import numpy as np
import math
import matplotlib.pyplot as plt


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
    return X


def index(fs, L, S, T, F):
    fn = fs/2
    F_ = np.arange(0, fn + (fn / F), fn / F)
    smp = (T - 1) * S + L
    T_ = np.arange(0,  smp / fs, smp / (fs * T))
    return F_, T_


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

F, T = index(fs, L, S, X.shape[0], X.shape[1])
F = np.round(F, 0)
T = np.round(T, 3)

fig, ax = plt.subplots(figsize=(5, 5))
spec = ax.pcolormesh(X, Y, 20 * np.log10(np.abs(C)).T, cmap="magma")
cb = fig.colorbar(spec, ax=ax, orientation="vertical")

plt.xticks(np.arange(X.shape[0]))
plt.yticks([0, 125, 251, 376, 501])
plt.xlabel("[sec]")
plt.ylabel("[Hz]")

F_ = np.array([F[0], F[125], F[251], F[376], F[502]])
ax.set_xticklabels(T)
ax.set_yticklabels(F_)
plt.show()
