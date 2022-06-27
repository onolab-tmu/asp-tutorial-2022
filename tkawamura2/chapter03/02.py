import numpy as np


def circ_conv(x, h):
    N = x.size
    M = h.size
    z = np.zeros(M)
    for n in range(M):
        for k in range(N):
            z[n] = z[n] + x[k]*h[np.mod(n-k, M)]
    return z
