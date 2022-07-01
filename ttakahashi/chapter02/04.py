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


delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])
delta_dft = dft(delta)
amp = np.abs(delta_dft)
phase = np.angle(delta_dft)

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.stem(amp)
ax2.stem(phase)
ax1.set_title("amplitude")
ax2.set_title("phase")
ax1.set_xlabel("k")
ax2.set_xlabel("k")
ax1.set_ylabel("amplitude spectrum")
ax2.set_ylabel("phase spectrum")
ax1.grid(True)
ax2.grid(True)
fig.tight_layout()
plt.savefig("outputs/04.pdf")
plt.show()

print("success!")
