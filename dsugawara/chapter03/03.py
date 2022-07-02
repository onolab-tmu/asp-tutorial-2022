import numpy as np


def Circar_convolution_padded(x, h):

    x = np.pad(x, [0, h.size - 1])
    h = np.pad(h, [0, x.size - 1])
    N = x.size
    z = np.zeros(N)

    for n in range(0, N):
        for k in range(0, N):
            z[n] += x[k] * h[(n - k) % N]

    return z
