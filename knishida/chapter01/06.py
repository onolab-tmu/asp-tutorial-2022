import numpy as np
import matplotlib.pyplot as plt

A = 1
f = 440.0
sec = 3.0
fs = 16000

t = np.arange(0, sec, 1 / fs)
y = A * np.sin(2 * np.pi * f * t)

n = np.random.rand(round(fs * sec))

plt.plot(t, y + n)
plt.xlim(0, 0.03)
plt.show()
