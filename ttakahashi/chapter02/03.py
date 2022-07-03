import numpy as np
import matplotlib.pyplot as plt


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


delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])
delta_dft = dft(delta)
delta_idft = idft(delta_dft)

plt.stem(np.arange(len(delta_idft)), delta_idft)
plt.xlabel("n")
plt.ylabel("amplitude")
plt.grid()
plt.savefig("outputs/03.pdf")
plt.show()

print("success!")
