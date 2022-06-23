import numpy as np


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
    x = np.random.randn(N)
    c = DFT(x)
    X = np.fft.fft(x)
    x_ifft = np.fft.ifft(c)
    c_i = IDFT(c)

    print(c)
    print(X)
