import numpy as np


def eq(a, b, x):
    N = len(a)
    M = len(b)
    L = len(x)
    y = np.zeros(L)
    for i in range(L):
        a_sum = 0
        b_sum = 0
        for j in range(1, N + 1):
            if i - j >= 0:
                a_sum += a[j] * y[i - j]
        for k in range(M + 1):
            if i - k > 0 and i - j <= L:
                b_sum += b[k] * x[i - k]

        y[i] = (-1 * a_sum + b_sum) / a[0]

    return y
