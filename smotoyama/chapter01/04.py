import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    fs = 16000
    s = 3

    t = np.arange(0, s, 1/fs)
    n = x = np.random.rand(round(fs * s))

    plt.plot(t, n)
    plt.show()
