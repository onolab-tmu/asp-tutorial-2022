import numpy as np
import matplotlib.pyplot as plt


def adjust_amp(x, snr, fs=16000, sec=3):
    whitenoise = np.random.rand(int(fs * sec)) * 2 - 1
    a = np.sqrt(np.sum(x**2) / np.sum(whitenoise**2) * (10 ** (-snr / 10)))
    whitenoise = a * np.random.rand(int(fs * sec)) - (a / 2)
    return whitenoise


def zero_pad(x, L, S):
    x_pad = np.pad(x, L - S)
    if x_pad.shape[0] % S != 0:
        x_pad = np.pad(x_pad, ((0, S - (x_pad.shape[0] % S))))
    return x_pad


def frame_div(x, L, S):
    x_pad = zero_pad(x, L, S)
    T = (x_pad.shape[0] - L) // S
    x_div = []
    for nT in range(T):
        x_t = []
        for nL in range(L):
            x_t.append(x_pad[nT * S + nL])
        x_div.append(x_t)
    return np.array(x_div)


def stft(x, L, S, win):
    x_div = frame_div(x, L, S)
    T = x_div.shape[0]
    X = []
    for t in range(T):
        tmp = x_div[t, :]
        tmp = tmp * win
        tmp = np.fft.rfft(tmp)
        X.append(tmp)
    return np.array(X).T


def composite_win(S, win):
    L = win.shape[0]
    Q = L // S
    for nL in range(L):
        sum = 0
        for nQ in range(Q):
            sum += win[nL - nQ * S] ** 2
    win_s = win / sum
    return np.array(win_s)


def istft(X, S):
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x = np.zeros((M))
    z = np.zeros((T, N))
    w_s = composite_win(S, win=np.hanning(N))
    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] = x[t * S + n] + w_s[n] * z[t, n]
    return x


fs = 16000
sec = 1
A = 1
fin = 440
t = np.linspace(0, sec, fs * sec)
N = fs * sec

s = A * np.cos(2 * np.pi * fin * t)
e = adjust_amp(s, 10, fs, sec)

x_1 = s + e

x_2 = np.zeros((N))
for n in range(N):
    x_2[n] = s[n - 10] + e[n]


x_3 = np.zeros((N))
for n in range(N):
    x_3[n] = s[n - 20] + e[n]

L = 1024
S = 512
win = np.hanning(L)

X_1 = stft(x_1, L, S, win)
X_2 = stft(x_2, L, S, win)
X_3 = stft(x_3, L, S, win)


x = np.stack([X_1, X_2, X_3])

F, T = x.shape[1], x.shape[2]
w = np.zeros((F, 3)).astype(np.complex128)
tau = np.array([0, 10 / fs, 20 / fs])
Y = np.zeros((F, T)).astype(np.complex128)
for f in range(F):
    for i in range(3):
        w[f, i] = 1 / 3 * np.exp(-1j * 2 * np.pi * f * fs / 2 / (F - 1) * tau[i])
    Y[f, :] = np.conj(w[f, :]).T @ x[:, f, :]

y = istft(Y, S)

plt.plot(np.linspace(0, sec, y.shape[0]), y)
plt.xlim(0, 0.1)
plt.show()
