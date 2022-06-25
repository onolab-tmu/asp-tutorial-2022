from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

A = 1  # 振幅
f = 440  # 周波数
sec = 3  # 長さ
fs = 16000  # サンプリング周波数

t = np.arange(0, sec, 1 / fs)  # 時間インデックス

xt = A * np.sin(2 * np.pi * f * t)  # 正弦波

xt_db = 20 * np.log10(np.abs(xt))

Xk = np.fft.fft(xt)

# 振幅スペクトル
plt.subplot(2, 1, 1)
plt.stem(np.abs(Xk))

# 位相スペクトル
plt.subplot(2, 1, 2)
plt.stem(np.angle(Xk))

plt.show()
