import numpy as np


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
    swin = syn_win(win, S)
    x = np.zeros(M, dtype=np.float64)
    z = np.empty([T, N], dtype=np.float64)
    for t in range(T):
        z[t] = np.fft.irfft(X[:, t])
        x[t * S: t * S + N] = x[t * S: t * S + N] + swin * z[t]
    return x
