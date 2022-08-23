import numpy as np


def syn_wnd(wnd, S):
    L = len(wnd)
    Q = L // S
    swnd = np.zeros(L)
    for i in range(L):
        k = i - (Q - 1) * S
        if k < 0:
            k = 0
        swnd[i] = wnd[i] / np.sum(wnd[k : i + (Q - 1) * S] ** 2)
    return swnd


def istft(S, X):
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    swnd = syn_wnd(np.hamming(N), S)
    x = np.zeros(M, dtype="complex")
    z = np.zeros((T, N), dtype="complex")
    for t in range(T):
        z[t] = np.fft.irfft(X[:, t])
        x[t * S : t * S + N] += swnd * z[t]
    return x
