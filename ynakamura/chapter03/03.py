import numpy as np


def zeropad_circular_conv(x, h):
    x = np.pad(x, (0, x.shape[0] - 1))
    h = np.pad(h, (0, h.shape[0] - 1))
    N = x.shape[0]
    z = np.array([])
    for n in range(N):
        sum = 0
        for k in range(N - 1):
            sum += x[k] * h[(n - k) % N]
        z = np.append(z, sum)
    return z
