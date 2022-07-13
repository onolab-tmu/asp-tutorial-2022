import numpy as np


def mix_win(w, S):
    L = len(w)
    Q = L // S
    ws = np.zeros(L)
    for l in range(L):
        a = l - (Q - 1)
        if a >= 0:
            ws[l] = w[l] / np.sum(w[a:Q] ** 2)
    return ws


def istft(X, S):
    F = X.shape[0]
    T = X.shape[1]

    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x = np.zeros(M, dtype=complex)
    z = np.zeros((T, N), dtype=complex)

    w = np.hamming(S)
    w = mix_win(w, S)

    for t in range(T):
        for n in range(N):
            z[t][n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] = x[t * S + n] + w[n] * z[t][n]

    return x
