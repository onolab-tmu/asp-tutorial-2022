import numpy as np
import matplotlib.pyplot as plt


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成

N = sec * sr
w = hamming(N)
y_wnd = y * w

plt.plot(y_wnd)
plt.xlabel("time [sec]")
plt.ylabel("amplitude")
plt.grid()
plt.savefig("outputs/08.pdf")
plt.show()

print("success!")
