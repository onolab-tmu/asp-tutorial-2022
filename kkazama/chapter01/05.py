import numpy as np
import matplotlib.pyplot as plt

A = 1    #振幅
sec = 3  #信号の長さ
fs = 16000 #サンプリング周波数

x = 2 * A * (np.random.rand(round(fs*sec)) - 0.5) #ホワイトノイズの生成

plt.plot(x)
plt.show()
