import numpy as np
import matplotlib.pyplot as plt

sec = 3.0
fs = 16000

t = np.arange(0, sec, 1 / fs)
n = np.random.rand(round(fs * sec))

plt.plot(t, n)
plt.show()
