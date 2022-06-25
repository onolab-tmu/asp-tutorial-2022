##################################################################
##### @ref https://take-tech-engineer.com/python-whitenoise/ #####
##### @author Tomohiro Takahashi 2022/06/14                  #####
##################################################################

import numpy as np
import matplotlib.pyplot as plt

sec = 3.0  # 信号の長さ s
sr = 16000 # サンプリング周波数 Hz

t = np.linspace(0, sec, sr)   # サンプリング点の生成
x = np.random.rand(round(sr)) # ホワイトノイズの生成

plt.xlim(0, 0.03)
plt.plot(t, x)
plt.show()
plt.savefig('output/05.svg')

print('success!')