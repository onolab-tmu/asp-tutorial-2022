import numpy as np
import matplotlib.pyplot as plt

a = 1     #振幅
fs = 16000 #サンプリング周波数
f = 440  #周波数
sec = 1   #秒 3→１

x = np.arange(sec*fs)/fs
y = np.sin(2*x*np.pi*f)

Y = np.fft.fft(y)

plt.plot(x, 20*np.log10(np.abs(Y)))
plt.show()

plt.plot(x, 20*np.log10(np.angle(Y)))
plt.show()