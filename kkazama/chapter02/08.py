from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

def hamm(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w

A = 1 #振幅
f = 440 #周波数
sec = 3 #長さ
fs = 16000 #サンプリング周波数

t = np.arange(0, sec, 1/fs) #時間インデックス

xt = A * np.sin(2 * np.pi * f * t) #正弦波

#窓関数
ham = hamm(fs * sec)

xt = xt * ham

plt.plot(xt)
plt.show()