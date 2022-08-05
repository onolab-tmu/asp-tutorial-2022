import numpy as np
import matplotlib.pyplot as plt


def set_snr(s, snr):
    A_s = np.linalg.norm(s)
    x = np.random.randn(round(len(s)))
    x = A_s * x / (10 ** (snr / 20) * np.linalg.norm(x))
    return x


a = 1     # 振幅
fs = 16000  # サンプリング周波数
f = 440  # 周波数
sec = 1   # 秒
snr = 10

x = np.arange(sec * fs) / fs
y = np.sin(2 * x * np.pi * f)

white_noise = set_snr(y, snr)

x1 = y + white_noise
x2 = np.pad(y[:-9], (9, 0)) + white_noise
x3 = np.pad(y[:-19], (19, 0)) + white_noise

plt.plot(x1)
plt.plot(x2)
plt.plot(x3)
plt.xlim(0, 0.01 * fs)
plt.show()
