from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

A = 1 #振幅
f = 440 #周波数
sec = 3 #長さ
fs = 16000 #サンプリング周波数

t = np.arange(0, sec, 1/fs) #時間インデックス

xt = A * np.sin(2 * np.pi * f * t) #正弦波

plt.xlim(0, 0.03) #軸範囲
plt.plot(t, xt)
plt.show()
