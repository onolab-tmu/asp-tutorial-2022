import numpy as np
import matplotlib.pyplot as plt

a = 1     #振幅
fs = 16000 #サンプリング周波数
f = 440  #周波数
sec = 3   #秒

x = np.arange(0, sec, 1/fs)
y = np.sin(2*x*np.pi*f)

plt.figure()
plt.plot(x, y)
plt.xlim([0, 0.03])
plt.show()