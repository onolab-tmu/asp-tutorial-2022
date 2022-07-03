import numpy as np
import matplotlib.pyplot as plt


fs = 16000
sec = 3
fin = 440
t = np.arange(sec * fs) / fs

x = np.sin(2.0 * np.pi * fin * t)

X = np.fft.fft(x)

# 振幅スペクトルの出力
plt.stem(20 * np.log10(np.abs(X)))
plt.title("amp")
plt.show()

# 位相スペクトルの出力
plt.stem(20 * np.log10(np.angle(X)))
plt.title("angle")
plt.show()
