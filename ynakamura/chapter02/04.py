import numpy as np
import matplotlib.pyplot as plt


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


N = 8
delta = np.zeros(N)
delta[0] = 1
Delta = dft(delta)

# 振幅スペクトルの出力
plt.stem(20 * np.log10(np.abs(Delta)))
plt.title("amp")
plt.show()

# 位相スペクトルの出力
plt.stem(20 * np.log10(np.angle(Delta)))
plt.title("angle")
plt.show()
