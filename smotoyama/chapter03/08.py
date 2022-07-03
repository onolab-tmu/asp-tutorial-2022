import numpy as np


def eq(a, b, f, fs):
    N = len(a)
    M = len(b)
    omega = 2 * np.pi * f / fs
    a_sum = 1
    b_sum = 0
    for i in range(1, N):
        a_sum += a[i] * np.exp(-1j * omega * i)
    for k in range(M):
        b_sum += b[k] * np.exp(-1j * omega * k)

    H = b_sum / a_sum

    return H
