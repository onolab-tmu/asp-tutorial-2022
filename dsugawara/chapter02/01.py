import numpy as np


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


# 確認
N = 8
x = np.random.randn(N)
c = dft(x)
X = np.fft.fft(x)
x_ifft = np.fft.ifft(c)
c_i = idft(c)

print(c)
print(X)
