import numpy as np
import matplotlib.pyplot as plt

A = 1    #振幅
f = 440
sec = 3  #信号の長さ
fs = 16000 #サンプリング周波数

x = 2 * A * (np.random.rand(round(fs*sec)) - 0.5) #ホワイトノイズの生成

t = np.arange(0, sec, 1/fs) #時間インデックス

s = A * np.sin(2 * np.pi * f * t) #正弦波

plt.plot(t, s)
plt.plot(t, x)
plt.xlim(0, 0.03) #軸範囲
plt.show()
