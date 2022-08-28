import numpy as np
import matplotlib.pyplot as plt


# DFT
def dft(f):
    N = len(f)
    X = np.zeros(N) * 1j
    for k in range(N):
        x = 0j
        for n in range(N):  # シグマ計算
            a = (2 * np.pi * n * k) / N
            x += f[n] * np.e ** (-1j * a)
        X[k] = x
    return X


# IDFT
def idft(F):
    N = len(F)
    x = np.zeros(N) * 1j
    for k in range(N):
        X = 0j
        for n in range(N):
            a = (2 * np.pi * n * k) / N
            X += 1 / N * F[n] * np.e ** (1j * a)
        x[k] = X
    return x


# impulse
delta = np.zeros(8)
delta[0] = 1
DELTA = dft(delta)
idft_delta = idft(DELTA)


# plot
plt.stem(idft_delta)
plt.savefig("03py_impulse_idft.png")
