import numpy as np
import matplotlib.pyplot as plt


def hamming(N):
    w = 0.54 - 0.46 * np.cos(2 * np.pi * np.arange(N) / (N-1))
    return w


a = 1  # 振幅
fs = 16000  # サンプリング周波数
f = 440  # 周波数
sec = 1  # 秒 3→１

x = np.arange(sec*fs)/fs
y = np.sin(2*x*np.pi*f)

y_win = y*hamming(len(y))

plt.plot(x, y_win)
plt.show()
