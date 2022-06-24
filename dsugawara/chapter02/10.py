import numpy as np
import matplotlib.pyplot as plt


# Humming窓
def Humming(N):
    w = []
    for n in range(N):
        a = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
        w.append(a)
    return w


# 第１章１. の信号
A = 1.0
f = 440.0
sf = 16000
sec = 3.0

t = np.arange(0, sec, 1 / sf)

y = A * np.sin(2 * np.pi * f * t)

dft_y = np.fft.fft(y)


# 窓関数
win = Humming(len(y))

dft_win = np.fft.fft(win)


# 畳み込み
dft_y = np.pad(dft_y, [int(len(dft_y) / 2), int(len(dft_y) / 2 - 1)])
conv = np.convolve(dft_y, dft_win, "valid")

idft_conv = np.fft.ifft(conv)


# plot
plt.plot(t, idft_conv.real)
plt.savefig("10py_convolution")
