#################################################################################
##### @ref https://numpy.org/doc/stable/reference/generated/numpy.mean.html #####
#####      https://ai-inter1.com/numpy-index/                               #####
##### @author Tomohiro Takahashi 2022/06/16                                 #####
#################################################################################

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


# Function to calculate SNR
def calc_snr(s, x):
    return 10*np.log10(np.sum(s**2)/np.sum(x**2))


# Function to adjust the amplitude of white noise to match the SNR
def adjust_snr(s, x, snr):
    return (x/np.sqrt(np.sum(x**2))) * np.sqrt(np.sum(s**2)) * 10**(-snr/20)


sec = 3.0  # 信号の長さ s
sr = 16000 # サンプリング周波数 Hz

t = np.linspace(0, sec, sr)   # サンプリング点の生成
x = np.random.rand(round(sr)) # ホワイトノイズの生成

y, sr = sf.read('output/02.wav')
s = x + y
adj_x = adjust_snr(s, x, 6)

M = 5
maf_x = []
for i in range(len(adj_x) - M):
    maf_x.append(np.mean(adj_x[i:i+M]))
for i in range(M):
    maf_x.append(maf_x[-1])

plt.xlim(0, 0.03)
plt.plot(t, adj_x)
plt.plot(t, maf_x)
plt.show()
plt.savefig('output/10.svg')

print('success!')