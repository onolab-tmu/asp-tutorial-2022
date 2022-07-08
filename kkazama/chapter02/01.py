from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

# DFT
def dft(x):
    N = len(x)  # 配列の長さ
    X = []  # 値代入用

    for n in range(N):
        a = -1j * 2 * np.pi * np.arange(N) * n
        X.append(np.sum(x[n] * np.exp(a / N)))

    return X


# IDFT
def idft(X):
    N = len(X)
    x = []
    for n in range(N):
        a = 1j * 2 * np.pi * np.arange(N) * n
        x.append(1 / N * np.sum(X[n] * np.exp(a / N)))

    return x
