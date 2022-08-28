import numpy as np


def dft(x):
    N = len(x)
    n = np.arange(N)
    dft_x = np.zeros(N, dtype=complex)
    for k in range(N):
        dft_x[k] = np.sum(x[n] * np.exp(-1j * 2 * np.pi * k * n / N))
    return dft_x


def idft(x):
    N = len(x)
    k = np.arange(N)
    idft_x = np.zeros(N, dtype=complex)
    for n in range(N):
        idft_x[n] = 1 / N * np.sum(x[k] * np.exp(1j * 2 * np.pi * k * n / N))
    return idft_x
