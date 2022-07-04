import numpy as np


def Liner_convolution(x, h):
    N = x.size
    z = np.zeros(2 * (N - 1))

    for n in range(2 * (N - 1)):
        for k in range(N):
            if 0 <= n - k and n - k <= N - 1:
                z[n] += x[k] * h[n - k]

    return z
