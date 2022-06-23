import numpy as np
import matplotlib.pyplot as plt


def DFT(x):
    N = len(x)
    c = np.zeros(N) * 1j

    for i in range(N):
        c[i] = np.sum(x * np.exp(-1j * 2 * np.pi * i * np.arange(N) / N))

    return c


def IDFT(X):
    N = len(X)
    c = np.zeros(N) * 1j

    for i in range(N):
        c[i] = (1 / N) * np.sum(X * np.exp(1j * 2 * np.pi * i * np.arange(N) / N))

    return c


if __name__ == "__main__":
    N = 8
    delta = np.zeros(N)
    delta[0] = 1

    c = DFT(delta)
    c_idft = IDFT(c)

    plt.stem(c_idft)
    plt.show()
