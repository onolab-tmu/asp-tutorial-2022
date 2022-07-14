from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt


def freq_res(a, b, f, fs):
    N = len(a)
    M = len(b)
    omega = (2 * np.pi * f) / fs

    sum_a = np.sum(a * np.exp(-1j * omega * np.arange(N))) - a[0]
    sum_b = np.sum(b * np.exp(-1j * omega * np.arange(M)))

    r = sum_b / (1 + sum_a)

    return r


N = 10
fs = 16000
H = np.zeros(N)
a = np.zeros(N)
b = np.zeros(N) + 0.2

for n in range(N):
    f = n * fs / N
    H[n] = freq_res(a, b, f, fs)

plt.subplot(2, 1, 1)
plt.stem(np.abs(H))

plt.subplot(2, 1, 2)
plt.stem(np.angle(H))

plt.show()
