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
N = len(y)
n = np.arange(0, N)
Z = np.empty(0)
dft_y = np.pad(dft_y, [int(len(dft_y) / 2), int(len(dft_y) / 2 - 1)])
for k in range(0, N):
    temp = np.sum(dft_y[n] * dft_win[(k - n) % N])
    Z = np.append(Z, temp)

idft_z = np.fft.ifft(Z)

plt.plot(t, idft_z)
plt.savefig("10py_circle_convolution.png")
