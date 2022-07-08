from wsgiref.headers import tspecials
import numpy as np


def freq_res(a, b, f, fs):
    N = len(a)
    M = len(b)
    omega = (2 * np.pi * f) / fs

    sum_a = np.sum(a * np.exp(-1j * omega * np.arange(1, N)))
    sum_b = np.sum(b * np.exp(-1j * omega * np.arange(M)))

    r = sum_b / (1 + sum_a)

    return r
