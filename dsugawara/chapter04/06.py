import numpy as np


def optimal_window(S, win):

    L = win.size
    Q = L // S
    for l in range(0, L):
        sigma = 0
        for m in range(0, Q):
            sigma += win[l - m * S] ** 2
    win_s = win / sigma

    return win_s


def istft(S, X):
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    win = np.hamming(N)
    win_opt = optimal_window(S, win)
    x = np.zeros(M)
    z = np.empty((T, N))

    for t in range(0, T):
        for n in range(0, N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] += win_opt[n] * z[t, n]

    return x
