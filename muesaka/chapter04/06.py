import numpy as np


def synthetic_window(S, w):
    L = len(w)
    Q = int(L / S)
    w_s = np.empty(L, dtype=float)
    for i in range(L):
        w_s[i] = 0
        for m in range(-(Q - 1), Q):
            if i - m * S < L:
                w_s[i] += w[i - m * S] ** 2
        w_s[i] = w[i] / w_s[i]
    return w_s


def istft(S, X):
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x_hat = np.zeros(M, dtype=complex)
    z = np.zeros((T, N), dtype=complex)
    w = np.hamming(N)
    w_s = synthetic_window(S, w)

    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x_hat[t * S + n] = x_hat[t * S + n] + w_s[n] * z[n]

    return x_hat
