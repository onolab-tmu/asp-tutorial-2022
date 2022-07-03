import numpy as np
import matplotlib.pyplot as plt

A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成

plt.xlim(0, 0.03)
plt.plot(t, y)
plt.savefig("outputs/01.pdf")
plt.show()

print("success!")
