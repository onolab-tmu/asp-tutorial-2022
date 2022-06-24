import numpy as np
import matplotlib.pyplot as plt


# 第１章１. の信号
A = 1.0
f = 440.0
sf = 16000
sec = 3.0

t = np.arange(0, sec, 1/sf)

y = A * np.sin(2*np.pi*f*t)

Y = np.fft.fft(y)


# スペクトルを求める
amp = 20 * np.log10(np.abs(Y))
angle = 20 * np.log10(np.angle(Y))


# plot
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.stem(amp)
ax2.stem(angle)
ax1.set_title("amplitude")
ax2.set_title("angle")
fig.tight_layout()
plt.savefig("06py_spectrum.png")
