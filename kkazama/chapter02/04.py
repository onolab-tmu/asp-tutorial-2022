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


# インパルス信号
N = 8
delta = np.zeros(N)
delta[0] = 1
x_dft = dft(delta)  # DFT

plt.subplot(2, 1, 1)
plt.stem(np.abs(x_dft))
plt.subplot(2, 1, 2)
plt.stem(np.angle(x_dft))

plt.show()
