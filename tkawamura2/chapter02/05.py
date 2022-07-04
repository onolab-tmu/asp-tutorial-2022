import numpy as np
import matplotlib.pyplot as plt


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


a = 1  # 振幅
fs = 16000  # サンプリング周波数
f = 440  # 周波数
sec = 1  # 秒 3→1

x = np.arange(sec * fs) / fs
y = np.sin(2 * x * np.pi * f)

Y = dft(y)

plt.plot(x, 20 * np.log10(np.abs(Y)))
plt.show()

plt.plot(x, 20 * np.log10(np.angle(Y)))
plt.show()
