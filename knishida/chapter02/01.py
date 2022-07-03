import numpy as np


def DFT(x):
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N)
    for k in range(N):
        X[k] = np.sum(x * np.exp(-1j * 2 * np.pi * k * n / N))
    return X


def IDFT(X):
    N = len(X)
    k = np.arange(N)
    x = np.zeros(N)
    for n in range(N):
        x[n] = np.sum(X * np.exp(1j * 2 * np.pi * k * n / N)) / N
    return x
