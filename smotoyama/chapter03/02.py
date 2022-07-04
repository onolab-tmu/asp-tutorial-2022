import numpy as np


def circular_conv(x, h):
    N = len(x)
    z = np.zeros(N)
    for n in range(z.size):
        for k in range(z.size):
            z[n] += x[k] * h[(n - k) % N]
    return z
