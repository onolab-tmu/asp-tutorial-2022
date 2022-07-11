import numpy as np


# 関数
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


def clc_istft(X, S):
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
    ws = syn_wnd(np.hamming(N), S)

    for t in range(T):
        z[t] = np.fft.irfft(X[:, t])
        x_hat[t * S : t * S + N] += ws * z[t]

    return x_hat
