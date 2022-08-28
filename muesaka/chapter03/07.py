import numpy as np


def calculate_difference(a, b, x, y_size):
    N = len(a)
    M = len(b)
    L = len(x)
    y = np.zeros(y_size)

    for n in range(y_size):
        ay = 0
        bx = 0
        for k in range(1, N):
            if n >= k:
                ay -= a[k] * y[n - k]
        for k in range(0, M):
            if (n >= k) and (n - k < L):
                bx += b[k] * x[n - k]
        y[n] = (ay + bx) / a[0]

    return y
