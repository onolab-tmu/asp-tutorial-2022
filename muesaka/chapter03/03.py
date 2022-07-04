import numpy as np


def padding_circular_convolution(x_in, h):
    x = np.pad(x_in, ((0, len(x_in) - 2)))
    h = np.pad(h, ((0, len(x_in) - 2)))
    N = len(x)
    z = np.zeros(N)

    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z
