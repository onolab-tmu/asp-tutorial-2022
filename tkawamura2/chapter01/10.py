import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write

#from 08 import set_snr
def set_snr(s, snr):
    A_s = np.linalg.norm(s)
    x = np.random.randn(round(len(s)))
    x = A_s * x /(10**(snr/20)*np.linalg.norm(x))
    return x

sec = 3.0  # 信号の長さ s
sf = 16000 # サンプリング周波数 Hz
snr = 6

fs, si = read("660_440.wav")

t = np.arange(0, sec, 1/fs)
y_1 = si[:,0] + set_snr(si[:,0], snr)
y_2 = si[:,1] + set_snr(si[:,1], snr)

y_1 = np.convolve(y_1,np.ones(5)/5, mode='valid')
y_2 = np.convolve(y_2,np.ones(5)/5, mode='valid')

y_1 = np.pad(y_1, (0,len(t)-len(y_1)))
y_2 = np.pad(y_2, (0,len(t)-len(y_2)))

plt.plot(t, y_1)
plt.plot(t, y_2)
plt.xlim([0, 0.03])
plt.show()