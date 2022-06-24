#################################################
##### @author Tomohiro Takahashi 2022/06/16 #####
#################################################

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

sec = 3.0  # 信号の長さ s
sr = 16000 # サンプリング周波数 Hz

t = np.linspace(0, sec, sr)   # サンプリング点の生成
x = np.random.rand(round(sr)) # ホワイトノイズの生成

y, sr = sf.read('output/02.wav')


# Function to adjust the amplitude of white noise to match the SNR
def adjust_snr(s, x, snr):
    return (x/np.sqrt(np.sum(x**2))) * np.sqrt(np.sum(s**2)) * 10**(-snr/20)


print(adjust_snr(y, x, 1.7))
print(x)

print('success!')