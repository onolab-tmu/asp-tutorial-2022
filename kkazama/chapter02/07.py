from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

def hamm(N):
    w = np.zeros(N)
    for n in range(N):
        w[n] = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w

ham = hamm(6)

plt.plot(ham)
plt.show()