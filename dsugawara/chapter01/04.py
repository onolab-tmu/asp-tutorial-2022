# 振幅 1, 周波数 660 Hz の正弦波をサンプリング周波数 16kHz で 3 秒分作成し，1.で作成した信号と合わせて 2ch の wav ファイルとして保存せよ．

import numpy as np
import matplotlib.pyplot as plt
import soundfile


y1, samplerate = soundfile.read("02py_sin.wav")


# 振幅 1, 周波数 660 Hz の正弦波をサンプリング周波数 16kHz で 3 秒分作成
A = 1.0
f = 660
sf = 16000
sec = 3.0
t = np.arange(0, 3, 1 / sf)
y2 = A * np.sin(2 * np.pi * f * t)

y = np.array([y1, y2])
y = y.T

soundfile.write(file="04py_sin2ch.wav", data=y, samplerate=sf)
