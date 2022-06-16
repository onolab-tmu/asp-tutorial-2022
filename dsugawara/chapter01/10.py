# 9.の信号に対して 5 点移動平均フィルタを適用した結果と元の信号をプロットせよ．

import numpy as np
import matplotlib.pyplot as plt
import soundfile

x, x_samplerate = soundfile.read("09py_mixed.wav")

y = np.zeros(len(x))
M = 5
for i in range(M, len(y)):
    y[i] = np.mean(x[i-M:i])

sf = 16000
sec = 1.0
t = np.arange(0, sec, 1/sf)

plt.plot(t, x)
plt.plot(t, y)
plt.xlim(0, 0.03)
plt.savefig("10py_filter.png")