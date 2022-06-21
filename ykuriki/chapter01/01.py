import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 16000
f = 440
r = 1
time = 3

t = np.arange(0, fs * time) / fs
sig = r * np.sin(f * 2 * np.pi * t)

# プロット
plt.plot(t, sig)
plt.xlim([0, 0.03])
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.grid()

plt.show()
