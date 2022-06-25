import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 16000
f = 440
r = 1
time = 3

np.random.seed(2286)

t = np.arange(0, fs * time) / fs
sig = r * np.sin(f * 2 * np.pi * t)
noise = np.random.rand(fs * time)
x = sig + noise

# プロット
plt.plot(t, x)
plt.xlim([0, 0.03])
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.grid()

plt.show()
