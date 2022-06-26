import numpy as np


# Function to calculate DFT
def dft(x):
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N, dtype="complex64")
    for k in range(N):
        X[k] = np.sum(x[n] * np.exp(-2j * np.pi * k * n / N))
    return X


# Function to calculate IDFT
def idft(X):
    N = len(X)
    k = np.arange(N)
    x = np.zeros(N, dtype="float64")
    for n in range(N):
        x[n] = np.sum(X[k] * np.exp(2j * np.pi * k * n / N)) / N
    return x


N = 8
x = np.random.rand(round(N))
x_dft = dft(x)
x_fft = np.fft.fft(x)
x_idft = idft(x_dft)
x_ifft = np.fft.ifft(x_fft)
print(x_idft)
print(x_ifft)

print("success!")
