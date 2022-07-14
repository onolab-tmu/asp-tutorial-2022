from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt


def hamm(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


# 窓関数
ham = hamm(48000)

ham_dft = np.fft.fft(ham)

plt.plot(ham_dft)
plt.show()
