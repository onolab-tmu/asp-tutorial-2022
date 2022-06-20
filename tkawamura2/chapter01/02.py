import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

a = 1     #振幅
fs = 16000 #サンプリング周波数
f = 440  #周波数
sec = 3   #秒

x = np.arange(0, sec, 1/fs)
y = np.sin(2*x*np.pi*f)

write("440.wav", fs, y)