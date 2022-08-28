import numpy as np


def dif_equation(x, a, b):
    L = x.shape[0]
    y = np.zeros((L))
    for n in range(L):
        sum1 = 0
        sum2 = 0
        for k in range(1, a.shape[0]):
            sum1 += a[k] * y[n - k]
        for k in range(b.shape[0]):
            sum2 += b[k] * x[n - k]
        y[n] = 1 / a[0] * (-sum1 + sum2)
    return y
