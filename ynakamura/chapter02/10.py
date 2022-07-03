import numpy as np
import matplotlib.pyplot as plt


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


def convolve(a, v):
    a_len = a.shape[0]
    v_len = v.shape[0]
    sum = np.array([])
    for i in range(a_len - v_len + 1):
        sum = np.append(sum, np.sum(a[i : v_len + i] * np.flip(v)))
    return sum


fs = 16000
sec = 3
fin = 440
t = np.arange(sec * fs) / fs

x = np.sin(2.0 * np.pi * fin * t)
w = hamming(x.shape[0])

X = np.fft.fft(x)
W = np.fft.fft(w)

X = np.pad(X, (X.shape[0] // 2, X.shape[0] // 2 - 1))

x_ham = np.fft.ifft(convolve(X, W))

plt.plot(t, x_ham)
plt.show()
