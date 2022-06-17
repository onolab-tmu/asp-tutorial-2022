import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

sec = 3.0  # 信号の長さ s
fs = 16000 # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs)
white = np.random.randn(round(fs*sec)) 
fs, si = read("660_440.wav")
y_1 = white + si[:,0]
y_2 = white + si[:,1]

plt.plot(t, y_1)
plt.plot(t, y_2)
plt.xlim([0, 0.03])
plt.show()
