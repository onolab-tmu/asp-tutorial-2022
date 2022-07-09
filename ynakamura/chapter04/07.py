import numpy as np
import matplotlib.pyplot as plt


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
    w_s = composite_win(S, win=np.hamming(N))
    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] = x[t * S + n] + w_s[n] * z[t, n]
    return x


fs = 16000  # サンプリング周波数
sec = 0.1  # 秒数
fin = 440  # 入力信号の周波数
a = 1.0  # 振幅
t = np.linspace(0.0, sec, int(fs * sec))
x = a * np.cos(np.pi * fin * t)

L = 1000
S = 500
win = np.hamming(L)
X = stft(x, L, S, win)

x = istft(X, S)

plt.plot(x)
plt.show()
