import numpy as np


def Difference_equation(x, a, b):
    N = a.size
    M = b.size
    L = x.sixe
    y = np.zeros(L)
    sigma_a = 0
    sigma_b = 0

    for n in range(0, L):
        # a[N]を含むシグマ計算
        for k in range(1, N):
            sigma_a += a[k] * y[n - k]
        # b[M]を含むシグマ計算
        for k in range(0, M):
            sigma_b += b[k] * x[n - k]

        y[n] = 1 / a[0] * (-1 * sigma_a + sigma_b)

    return y
