import numpy as np


def freq_response(a, b, fs, f):
    w = 2 * np.pi * f / fs
    W = np.exp(1j * w)

    sum1 = 0
    for k in range(1, a.shape[0]):
        sum1 += a[k] * np.exp(W * -k)

    sum2 = 0
    for k in range(b.shape[0]):
        sum2 += b[k] * np.exp(W * -k)

    H = sum2 / (1 + sum1)
    return H
