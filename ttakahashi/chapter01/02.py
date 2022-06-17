####################################################################
##### @ref https://www.wizard-notes.com/entry/python/soundfile #####
##### @author Tomohiro Takahashi 2022/06/14                    #####
####################################################################

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

A = 1      # 振幅
f = 440    # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000 # サンプリング周波数 Hz

t = np.linspace(0, sec, sr) # サンプリング点の生成
y = A*np.sin(2*np.pi*f*t)   # 正弦波の生成

sf.write('output/02.wav', y, sr, format='WAV', subtype='PCM_16')

print('success!')