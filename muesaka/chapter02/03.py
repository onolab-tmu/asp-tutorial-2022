import numpy as np
import matplotlib.pyplot as plt


def dft(x):
    N = len(x)
    n = np.arange(N)
    dft_x = np.zeros(N, dtype=complex)
    for k in range(N):
        dft_x[k] = np.sum(x[n] * np.exp(-1j * 2 * np.pi * k * n / N))
    return dft_x


def idft(x):
    N = len(x)
    k = np.arange(N)
    idft_x = np.zeros(N, dtype=complex)
    for n in range(N):
        idft_x[n] = 1 / N * np.sum(x[k] * np.exp(1j * 2 * np.pi * k * n / N))
    return idft_x


if __name__ == "__main__":
    delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])  # インパルス信号

    dft_delta = dft(delta)
    idft_delta = idft(dft_delta)

    plt.stem(idft_delta.real)
    plt.xlabel("index")
    plt.ylabel("amplitude")
    plt.show()
