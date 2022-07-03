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
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp((-2j * np.pi * k * n) / N)
    return X


if __name__ == '__main__':
    x = np.array([1, 0, 0, 0, 0, 0, 0, 0])
    X = dft(x)
    X_amp = 20 * np.log10(np.abs(X))
    X_phase = 20 * np.log10(np.angle(X))
    plt.subplot(2, 1, 1)
    plt.stem(X_amp)
    plt.grid()
    plt.title("Amplitude")
    plt.subplot(2, 1, 2)
    plt.stem(X_phase)
    plt.grid()
    plt.title("Phase")
    plt.show()
