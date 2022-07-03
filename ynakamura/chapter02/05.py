import numpy as np


N = 8
delta = np.zeros(N)
delta[0] = 1
Delta = np.fft.fft(delta)

print(Delta)
