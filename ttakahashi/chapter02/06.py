import numpy as np
import matplotlib.pyplot as plt

A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成
y_fft = np.fft.fft(y)
amp = 20 * np.log10(np.abs(y_fft))
phase = 20 * np.log10(np.angle(y_fft))

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.plot(amp)
ax2.plot(phase)
ax1.set_title("amplitude")
ax2.set_title("phase")
ax1.set_xlabel("k")
ax2.set_xlabel("k")
ax1.set_ylabel("amplitude spectrum [db]")
ax2.set_ylabel("phase spectrum [db]")
ax1.grid(True)
ax2.grid(True)
fig.tight_layout()
plt.savefig("outputs/06.pdf")
plt.show()

print("success!")
