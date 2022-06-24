import numpy as np
import matplotlib.pyplot as plt

sec = 3.0  # 信号の長さ s
fs = 16000 # サンプリング周波数 Hz

t = np.arange(0, sec, 1/fs)
x = np.random.randn(round(fs*sec)) 

plt.plot(t, x)
plt.xlim([0, 0.03])
plt.show()