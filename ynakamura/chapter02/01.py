import numpy as np


def dft(x):
    N = x.shape[0]
    X = np.array([])
    for k in range(N):
        sum = 0
        for n in range(N):
            sum += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
        X = np.append(X, sum)
    return X


def idft(X):
    N = X.shape[0]
    x = np.array([])
    for n in range(N):
        sum = 0
        for k in range(N):
            sum += X[k] * np.exp(1j * 2 * np.pi * k * n / N)
        x = np.append(x, sum / N)
    return x
