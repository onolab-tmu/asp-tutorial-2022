import numpy as np


def Circlar_convolution(x, h):

    N = x.size
    z = np.zeros(N)

    for n in range(0, N):
        for k in range(0, N):
            z[n] += x[k] * h[(n - k) % N]

    return z
