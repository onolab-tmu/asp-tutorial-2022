import numpy as np


def liner_conv(x, h):
    N = x.size
    M = x.size + h.size - 1
    z = np.zeros(M)
    for n in range(M):
        for k in range(N):
            if n-k >= 0 and n-k <= N - 1:
                z[n] = z[n] + x[k]*h[n-k]
    return z
