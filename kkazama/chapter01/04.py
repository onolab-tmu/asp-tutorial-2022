from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt
import soundfile as sf

A = 1 #振幅
f1 = 440 #周波数
f2 = 660
sec = 3 #長さ
fs = 16000 #サンプリング周波数

t = np.arange(0, sec, 1/fs) #時間インデックス

x1 = A * np.sin(2 * np.pi * f1 * t) #正弦波
x2 = A * np.sin(2 * np.pi * f2 * t)

y = np.array([x1, x2])
y = y.T

sf.write("stereo.wav", y, fs, subtype="PCM_16")

#波形確認
plt.subplot(3, 1, 1)
plt.plot(t, x1)
plt.xlim(0, 0.03) #軸範囲

plt.subplot(3, 1, 2)
plt.plot(t, x2)
plt.xlim(0, 0.03)

plt.subplot(3, 1, 3)
plt.plot(t, y)
plt.xlim(0, 0.03)

plt.show()