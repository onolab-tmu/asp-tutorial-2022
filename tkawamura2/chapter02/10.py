import numpy as np
import matplotlib.pyplot as plt


def convolve(x, y):
    N = x.size
    out = np.zeros(N + y.size, dtype=np.complex128)
    for n in range(y.size):
        out[n: n + N] += x * y[n]
    return out[:N]


def hamming(N):
    w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(N) / (N - 1))
    return w


a = 1  # 振幅
fs = 16000  # サンプリング周波数
f = 440  # 周波数
sec = 1  # 秒 3→１

x = np.arange(sec * fs) / fs
y = np.sin(2 * x * np.pi * f)

Y = np.fft.fft(y)
w = hamming(len(x))
W = np.fft.fft(w)

Y = np.pad(Y, [int(len(Y) / 2), int(len(Y) / 2 - 1)])

Y_win = np.convolve(Y, W, mode="valid")
# Y_win = convolve(Y, W)
y_win = np.fft.ifft(Y_win)

plt.plot(x, y_win.real)
plt.show()
