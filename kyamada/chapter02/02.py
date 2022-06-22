import numpy as np
import matplotlib.pyplot as plt


def dft(x):
    """
    DFT
    Input:
        x: input array
    Output:
        X: output DFT array
    """
    N = x.size
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp((-2j * np.pi * k * n) / N)
    return X


if __name__ == '__main__':
    x = np.array([1, 0, 0, 0, 0, 0, 0, 0])
    X = dft(x)
    plt.stem(X)
    plt.show()
