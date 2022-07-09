import numpy as np


def composite_win(S, win):
    L = win.shape[0]
    Q = L // S
    for nL in range(L):
        sum = 0
        for nQ in range(Q):
            sum += win[nL - nQ * S] ** 2
    win_s = win / sum
    return np.array(win_s)


def istft(X, S):
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x = np.zeros((M))
    z = np.zeros((T, N))
    w_s = composite_win(S, win=np.hamming(N))
    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] = x[t * S + n] + w_s[n] * z[t, n]
    return x
