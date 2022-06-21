import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

a = 1     #振幅
fs = 16000 #サンプリング周波数
f = 660  #周波数
sec = 3   #秒

x = np.arange(0, sec, 1/fs)
y_1 = np.sin(2*x*np.pi*f)

fs, y_2 = read("440.wav")

y_1 = y_1.reshape([len(y_1), 1])
y_2 = y_2.reshape([len(y_2), 1])

y = np.concatenate([y_1, y_2], axis=1)

write("660_440.wav", fs, y)
