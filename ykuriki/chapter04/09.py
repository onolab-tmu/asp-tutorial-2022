import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt


# 関数
def zero_pad(x, L, S):
    """x[n]に零詰めする

    Args:
        x (ndarray): 信号（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: 零詰めされた信号

    """
    x = np.block([np.zeros(L - S), x, np.zeros(L - S)])

    if len(x) % S != 0:
        x = np.block([x, np.zeros(S - (len(x) % S))])

    return x


def frame_div(x, L, S):
    """x[n]をフレーム分割する

    Args:
        x (ndarray): 信号（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: フレーム分割された信号

    """
    x = zero_pad(x, L, S)
    T = int(np.floor((len(x) - L) / S)) + 1
    xt = np.zeros((T, L))

    for t in range(T):
        xt[t] = x[t * S : t * S + L]

    return xt


def clc_stft(x, w, L, S):
    """x[n]のSTFTを計算する

    Args:
        x (ndarray): 信号（1次元配列）
        w (ndarray): 窓関数（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: x[n]のSTFT

    """
    x = frame_div(x, L, S)
    T = len(x)
    X = np.zeros((T, L // 2 + 1), dtype="complex")

    for t in range(T):
        X[t] = np.fft.rfft(x[t] * w)

    return X.T


def syn_wnd(w, S):
    """合成窓を生成する

    Args:
        w (ndarray): 窓関数
        S (int): シフト幅

    Returns:
        ws (ndarray): 合成窓（float型1次元配列）

    """
    L = len(w)
    Q = L // S
    ws = np.zeros(L)

    for l in range(L):
        tmp = 0
        for m in range(-Q + 1, Q):
            if l - m * S < L:
                tmp += w[l - m * S] ** 2
        ws[l] = w[l] / tmp

    return ws


def clc_istft2(X, S):
    """X[f,t]のISTFTを計算する

    Args:
        X (ndarray): F×Tの複素数行列
        S (int): シフト幅

    Returns:
        x_hat (ndarray): X[f,t]のISTFT

    """
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x_hat = np.zeros(M, dtype="complex")
    z = np.zeros((T, N), dtype="complex")
    ws = np.ones(N)

    for t in range(T):
        z[t] = np.fft.irfft(X[:, t])
        x_hat[t * S : t * S + N] += ws * z[t]

    return x_hat


fs = 16000
f0 = 100
f1 = 16000
sec = 1
L = np.array([100, 200, 400, 800])
S = np.array([50, 100, 200, 400])

t = np.arange(fs * sec) / fs
x = sp.chirp(t, f0, sec, f1)


# プロット
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))

for i in range(len(L)):
    w = np.hamming(L[i])
    X = clc_stft(x, w, L[i], S[i])

    p0 = ax[i // 2, i % 2].pcolormesh(20 * np.log10(np.abs(X)))
    ax[i // 2, i % 2].set_title(str(L[i]) + "/" + str(S[i]))

plt.tight_layout()

plt.show()
