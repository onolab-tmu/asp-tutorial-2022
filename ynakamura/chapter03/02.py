import numpy as np


def circular_conv(x, h):
    N = x.shape[0]
    z = np.array([])
    for n in range(N - 1):
        sum = 0
        for k in range(N):
            sum += x[k] * h[(n - k) % N]
        z = np.append(z, sum)
    return z
