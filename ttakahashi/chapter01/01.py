###############################################################
##### @ref https://take-tech-engineer.com/python-sin-wav/ #####
##### @author Tomohiro Takahashi 2022/06/14               #####
###############################################################

import numpy as np
import matplotlib.pyplot as plt

A = 1      # 振幅
f = 440    # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000 # サンプリング周波数 Hz

t = np.linspace(0, sec, sr) # サンプリング点の生成
y = A*np.sin(2*np.pi*f*t)   # 正弦波の生成

plt.xlim(0, 0.03)
plt.plot(t, y)
plt.show()
plt.savefig('output/01.svg')

print('success!')