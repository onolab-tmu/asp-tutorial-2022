from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt


def differ_eq(x, a, b):
    L = len(x)
    N = len(a)
    M = len(b)
    y = np.zeros(L)

    for n in range(L):

        for k in range(1, N):
            if n - k >= 0:
                y[n] -= a[k] * y[n - k]

        for l in range(M):
            if n - l >= 0 and n - l < L:
                y[n] += b[l] * x[n - l]

    y = y / a[0]

    return y


x = np.zeros(10)
x[0] = 1
a = np.zeros(10) + 0.3
b = np.zeros(10) + 0.4
y = differ_eq(x, a, b)

plt.stem(y)

plt.show()
