#################################################
##### @author Tomohiro Takahashi 2022/06/14 #####
#################################################

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

sec = 3.0  # 信号の長さ s
sr = 16000 # サンプリング周波数 Hz

t = np.linspace(0, sec, sr)   # サンプリング点の生成
x = np.random.rand(round(sr)) # ホワイトノイズの生成

y, sr = sf.read('output/02.wav')
s = x + y

plt.xlim(0, 0.03)
plt.plot(t, s)
plt.show()
plt.savefig('output/06.svg')

print('success!')