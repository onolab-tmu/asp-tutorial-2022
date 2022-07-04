import numpy as np


def circpad_linerconv(x, h):
    N = x.size
    h = np.pad(h, [0, int(N / 2) + 1])
    M = h.size
    z = np.zeros(M)
    for n in range(M):
        for k in range(N):
            z[n] = z[n] + x[k]*h[np.mod(n-k, M)]
    return z
