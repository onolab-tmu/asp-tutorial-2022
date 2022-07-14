import numpy as np


def linear_conv(x, h):
    N = x.shape[0]
    z = np.array([])
    for n in range(2 * N - 1):
        sum = 0
        for k in range(N):
            if n - k >= 0 and n - k <= N - 1:
                sum += x[k] * h[n - k]
            else:
                sum += 0
        z = np.append(z, sum)
    return z
