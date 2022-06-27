import numpy as np
import matplotlib.pyplot as plt


def Hamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return win


if __name__ == "__main__":
    A = 1
    f = 440.0
    sec = 3.0
    fs = 16000

    t = np.arange(0, sec * fs) / fs
    y = A * np.sin(2 * np.pi * f * t)

    win_ham = Hamming(len(y))
    y_ham = y * win_ham

    plt.plot(t, y_ham)
    plt.show()
