import numpy as np


# Function to calculate DFT
def dft(x):
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N, dtype="complex64")
    for k in range(N):
        X[k] = np.sum(x[n] * np.exp(-2j * np.pi * k * n / N))
    return X


delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])
delta_dft = dft(delta)
delta_fft = np.fft.fft(delta)
print(np.array_equal(delta_dft, delta_fft))

print("success!")
