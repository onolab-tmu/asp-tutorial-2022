import numpy as np
import matplotlib.pyplot as plt


fs = 16000
sec = 3
fin = 440
t = np.linspace(0.0, sec, int(fs * sec))

x = np.sin(2.0 * np.pi * fin * t)

plt.plot(t, x)
plt.xlim(0, 0.03)
plt.show()
