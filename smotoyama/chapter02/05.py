import numpy as np
import matplotlib.pyplot as plt


def DFT(x):
    N = len(x)
    c = np.zeros(N) * 1j

    for i in range(N):
        c[i] = np.sum(x * np.exp(-1j * 2 * np.pi * i * np.arange(N) / N))
        print(i)

    return c


def IDFT(X):
    N = len(X)
    c = np.zeros(N) * 1j

    for i in range(N):
        c[i] = (1 / N) * np.sum(X * np.exp(1j * 2 * np.pi * i * np.arange(N) / N))

    return c


if __name__ == "__main__":
    A = 1
    f = 440
    fs = 16000
    s = 3

    t = np.arange(0, s, 1 / fs)
    x = A * np.sin(2 * np.pi * f * t)

    X = DFT(x)

    X_amp = 20 * np.log10(np.abs(X))
    X_ang = 20 * np.log10(np.angle(X))

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.plot(X_amp)
    ax2.plot(X_ang)
    ax1.set_title("Amplitude Spectrum")
    ax2.set_title("Phase Spectrum")
    fig.tight_layout()
    plt.show()
