import numpy as np


def dft(x):
    N = len(x)
    X = np.empty(N, dtype=np.complex128)
    for k in range(N):
        X[k] = np.sum(x*np.exp(-2j*np.pi*k*np.arange(N)/N),
                      dtype=np.complex128)
    return X


def idft(X):
    N = len(X)
    x = np.empty(N, dtype=np.float64)
    for n in range(N):
        x[n] = np.sum(X*np.exp(2j*np.pi*n*np.arange(N)/N), dtype=np.float64)/N
    return x


delta = np.zeros(8, dtype=np.float64)
delta[0] = 1
Delta = dft(delta)
delta_ = idft(Delta)
print(delta_)
