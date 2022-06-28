import numpy as np
import matplotlib.pyplot as plt


def freq_response(a, b, fs, f):
    w = 2 * np.pi * f / fs
    W = np.exp(1j * w)

    sum1 = 0
    for k in range(1, a.shape[0]):
        sum1 += a[k] * np.exp(W * -k)

    sum2 = 0
    for k in range(b.shape[0]):
        sum2 += b[k] * np.exp(W * -k)

    H = sum2 / (1 + sum1)
    return H


a = np.array([1, -0.3])
b = np.array([0.4])
fs = 16000
N = 10
f = np.array([])
for n in range(N):
    f = np.append(f, n / N * fs)
H = freq_response(a, b, fs, f)


plt.stem(np.abs(H))
plt.title("Amp")
plt.show()

plt.stem(np.angle(H))
plt.title("Phase")
plt.show()
