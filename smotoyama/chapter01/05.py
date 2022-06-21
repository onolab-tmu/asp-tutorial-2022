import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    A = 1
    f = 440
    fs = 16000
    s = 3

    t = np.arange(0, s, 1 / fs)
    x = A * np.sin(2 * np.pi * f * t)
    n = np.random.rand(round(fs * s))

    y = x + n

    plt.plot(t, y)
    plt.show()
