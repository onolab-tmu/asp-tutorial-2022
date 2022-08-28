import numpy as np


def calculate_frequency_responce(a, b, f, fs):
    N = len(a)
    M = len(b)
    tmp_a = 0
    tmp_b = 0
    omega = 2 * np.pi * f / fs

    for k in range(0, M):
        tmp_b += b[k] * np.exp(-1j * omega * k)
    for k in range(1, N):
        tmp_a += a[k] * np.exp(-1j * omega * k)
    H = tmp_b / (1 + tmp_a)

    return H
