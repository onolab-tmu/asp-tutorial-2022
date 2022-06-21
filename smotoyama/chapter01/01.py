import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    A = 1
    f = 440
    fs = 16000
    s = 3

    t = np.arange(0, s, 1 / fs)
    x = x = A * np.sin(2 * np.pi * f * t)

    plt.plot(t, x)
    plt.show()
