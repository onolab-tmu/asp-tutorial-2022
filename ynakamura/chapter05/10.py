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


def calc_linear_vector(d, M, thete, f):
    c = 334

    u = np.array([np.sin(thete), np.cos(thete), 0])
    a = np.zeros((M)).astype(complex)
    for m in range(M):
        pm = np.array([((m - 1) - (M - 1) / 2) * d, 0, 0]).T
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ pm)

    return a


def calc_spatial_correlation_matrix(X):
    M, F, T = X.shape

    x = [0] * M
    for m in range(M):
        x[m] = X[m, :, :]
    x = np.array(x)

    R = []
    for f in range(F):
        sum = np.zeros((M, M)).astype(np.complex128)
        for t in range(T):
            tmp1 = x[:, f, t].reshape(-1, 1)
            tmp2 = np.conj(x[:, f, t]).reshape(-1, 1).T
            tmp3 = tmp1 @ tmp2
            sum += tmp3
        R.append(1 / T * sum)
    R = np.array(R)

    return R


def calc_spatial_spec(z, w):
    M, N = z.shape  # マイク数，サンプリング数
    F, _, M = w.shape  # 周波数ビンの総数，角度の総数，マイク数

    L = 1024
    S = 512
    win = np.hanning(L)

    Z = [0] * M
    for m in range(M):
        Z[m] = stft(z[m, :], L, S, win)
    Z = np.array(Z)

    M, F, T = Z.shape

    R = calc_spatial_correlation_matrix(Z)

    P = np.zeros((F, 361)).astype(np.complex128)
    for f in range(F):
        for theta in range(361):
            P[f, theta] = np.conj(w[f, theta, :]).T @ R[f, :, :] @ w[f, theta, :]

    for f in range(20, 31):
        plt.plot(np.arange(361), 20 * np.log10(np.abs(P[f, :])))
        plt.xlim(0, 360)
        plt.ylim(0, np.max(20 * np.log10(np.abs(P))))
        plt.xlabel("Direction [deg]")
        plt.ylabel("Spatial spec. [dB]")
        plt.title(f"f = {f}")
        plt.show()


M = 3
d = 0.05
F = 513


fs = 16000
sec = 1
A = 1
f = 440
t = np.linspace(0, sec, fs * sec)
N = fs * sec

s = A * np.cos(2 * np.pi * f * t)
e = adjust_amp(s, 10, fs, sec)

x_1 = s + e

x_2 = np.zeros((N))
for n in range(N):
    x_2[n] = s[n - 10] + e[n]


x_3 = np.zeros((N))
for n in range(N):
    x_3[n] = s[n - 20] + e[n]

z = np.stack([x_1, x_2, x_3])


a = np.zeros((F, 361, M)).astype(np.complex128)
for f in range(F):
    for theta in range(361):
        a[f, theta, :] = calc_linear_vector(d, M, theta, f)
w = a / M

calc_spatial_spec(z, w)
