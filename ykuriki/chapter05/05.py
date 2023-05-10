import numpy as np


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


def clc_sp_mat(X):
    """空間相関行列を計算する

    Args:
        X (ndarray): M個のF×T複素数行列


    Returns:
        R (ndarray): 空間相関行列

    """
    M, F, T = X.shape
    R = np.zeros((F, M, M), dtype="complex")

    for f in range(F):
        for t in range(T):
            x_ft = X[:, f, t]
            R[f] += np.outer(x_ft, np.conjugate(x_ft))
        R[f] /= T

    return R


fs = 16000
sec = 5
L = 512
S = 256

np.random.seed(2286)
noise1 = np.random.randn(fs * sec)
noise2 = np.random.randn(fs * sec)

w = np.hanning(L)

X1 = clc_stft(noise1, w, L, S)
X2 = clc_stft(noise2, w, L, S)
X = np.array([X1, X2])

R = clc_sp_mat(X)

print(R[100].real)
