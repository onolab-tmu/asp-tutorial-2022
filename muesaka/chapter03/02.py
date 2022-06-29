import numpy as np
import matplotlib.pyplot as plt


def circular_convolution(x, h):
    N = len(x)
    z = []
    for n in range(N):
        sum = 0
        for k in range(N):
            sum += x[k] * h[(n - k) % N]
        z = np.append(z, sum)
    return z


if __name__ == "__main__":
    x = np.array([4, 3, 2, 1])
    y = np.array([1, 0, -1, 0])
    z = circular_convolution(x, y)

    plt.stem(z)
    plt.show()
