import numpy as np


def dif_equ(x, a, b):
    L = x.size
    N = a.size
    M = b.size
    y = np.zeros(L)

    for n in range(L):
        for k1 in np.arange(1, N):
            if n-k1 >= 0:
                y[n] = y[n] - a[k1]*y[n-k1]
        for k2 in range(M):
            if n-k2 >= 0:
                y[n] = y[n] + b[k2]*x[n-k2]

    return y/a[0]
