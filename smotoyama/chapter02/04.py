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

    X = DFT(delta)

    X_amp = 20 * np.log10(np.abs(X))
    X_ang = 20 * np.log10(np.angle(X))

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.stem(X_amp)
    ax2.stem(X_ang)
    ax1.set_title("Amplitude")
    ax2.set_title("Angle")
    fig.tight_layout()
    plt.show()
