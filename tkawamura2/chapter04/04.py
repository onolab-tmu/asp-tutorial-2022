import numpy as np
import math
import matplotlib.pyplot as plt


def pad(x, L, S):
    x_ = np.pad(x, [L - S, L - S])
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
    return X


a = 1  # 振幅
fs = 16000  # サンプリング周波数
f = 440  # 周波数
sec = 0.1  # 秒

x = np.arange(sec * fs) / fs
y = np.sin(2 * x * np.pi * f)


L = 1000  # 窓長
S = 500  # ステップサイズ

C = my_stft(y, L, S)
X, Y = np.mgrid[: C.shape[1] + 1, : C.shape[0] + 1]

fig, ax = plt.subplots(figsize=(5, 5))
spec = ax.pcolormesh(X, Y, 20 * np.log10(np.abs(C)).T, cmap="magma")
cb = fig.colorbar(spec, ax=ax, orientation="vertical")

plt.show()
