import numpy as np


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w
