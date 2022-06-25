import numpy as np
import matplotlib.pyplot as plt


def Hamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return win


if __name__ == "__main__":
    A = 1
    f = 440
    fs = 16000
    s = 3

    t = np.arange(0, s, 1 / fs)
    x = A * np.sin(2 * np.pi * f * t)

    win = Hamming(len(x))

    plt.plot(win)
    plt.show()
