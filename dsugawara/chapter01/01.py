# 振幅 1, 周波数 440 Hz の正弦波をサンプリング周波数 16kHz で 3 秒分作成しプロットせよ．

import numpy as np
from matplotlib import pyplot as plt


A = 1.0
f = 440.0
sf = 16000
sec = 3.0

t = np.arange(0, sec, 1/sf)

y = A * np.sin(2*np.pi*f*t)

plt.xlim(0, 0.03)
plt.plot(t, y)
#plt.show()
plt.savefig("01py_sin.png")