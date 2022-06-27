import numpy as np


def frequency_responce(a, b, f, fs):
    N = len(a)
    M = len(b)
    tmpa = 0
    tmpb = 0
    omega = 2 * np.pi * f / fs
    for k in range(1, N):
        tmpa += a[k] * np.exp(-1j * omega * k)
    for k in range(M):
        tmpb += b[k] * np.exp(-1j * omega * k)
    H = tmpb / (1 + tmpa)
    return H
