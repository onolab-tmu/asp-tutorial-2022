from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

A = 1  # 振幅
f = 440  # 周波数
sec = 3  # 長さ
fs = 16000  # サンプリング周波数

t = np.arange(0, sec * fs) / fs  # 時間インデックス

xt = A * np.sin(2 * np.pi * f * t)  # 正弦波

Xk = np.fft.fft(xt)

amp = 20 * np.log10(np.abs(Xk))
angle = 20 * np.log(np.angle(Xk))

# 振幅スペクトル
plt.subplot(2, 1, 1)
plt.stem(amp)

# 位相スペクトル
plt.subplot(2, 1, 2)
plt.stem(angle)

plt.show()
