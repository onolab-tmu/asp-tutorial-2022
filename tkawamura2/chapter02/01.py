import numpy as np


def dft(x):
    N = len(x)
    X = np.empty(N, dtype=np.complex128)
    for k in range(N):
        X[k] = np.sum(x * np.exp(-2j * np.pi * k * np.arange(N) / N))
    return X


def idft(X):
    N = len(X)
    x = np.empty(N, dtype=np.float64)
    for n in range(N):
        x[n] = np.sum(X * np.exp(2j * np.pi * n * np.arange(N) / len(x))) / N
    return X
