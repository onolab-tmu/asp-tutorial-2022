import numpy as np
import math
import matplotlib.pyplot as plt


def syn_win(win, S):
    L = win.size
    Q = int(np.floor(L / S))
    swin = np.empty(L, dtype=np.float64)
    for i in range(L):
        k = i - (Q - 1) * S
        if k < 0:
            k = 0
        swin[i] = win[i] / np.sum(win[k: i + (Q - 1) * S]**2)
    return swin


def my_istft(X, S, win):
    T = X.shape[1]
    N = 2 * (X.shape[0] - 1)
    M = S * (T - 1) + N
    x = np.zeros(M, dtype=np.float64)
    z = np.empty([T, N], dtype=np.float64)
    for t in range(T):
        z[t] = np.fft.irfft(X[:, t])
        x[t * S: t * S + N] = x[t * S: t * S + N] + z[t]
    return x


def pad(x, L, S):
    x_ = np.pad(x, [L-S, L-S])
    a = np.mod(x_.size, S)
    if a != 0:
        x_ = np.pad(x_, [0, S - a])
    return x_


def frame_div(x, L, S):
    x_ = pad(x, L, S)
    N_ = x_.size
    T = math.floor((N_ - L) / S) + 1
    x_t = np.empty([T, L], dtype=np.float64)
    for t in range(T):
        x_t[t] = x_[t * S: t * S + L]
    return x_t


def my_stft(x, L, S):
    x_t = frame_div(x, L, S)
    T = x_t.shape[0]
    win = np.hamming(L)
    X = np.empty([int(np.floor(L / 2)) + 1, T], dtype=np.complex128)
    for t in range(T):
        X[:, t] = np.fft.rfft(win * x_t[t, :])
    return X, win


a = 1  # 振幅
fs = 16000  # サンプリング周波数
f = 440  # 周波数
sec = 0.1  # 秒

x = np.arange(sec * fs) / fs
y = np.sin(2 * x * np.pi * f)


L = 1000  # 窓長
S = 500  # ステップサイズ

C, win = my_stft(y, L, S)

y_ = my_istft(C, S, win)

plt.plot(y_)
plt.show()
