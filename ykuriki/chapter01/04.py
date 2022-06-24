import numpy as np
import matplotlib.pyplot as plt


# パラメータ
fs = 16000
time = 3

np.random.seed(2286)

t = np.arange(0, fs * time) / fs
noise = np.random.rand(fs * time)

# プロット
plt.plot(t, noise)
plt.xlim([0, 0.03])
plt.xlabel("time [s]")
plt.ylabel("amplitude")
plt.grid()

plt.show()
