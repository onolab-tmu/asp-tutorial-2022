import numpy as np
import matplotlib.pyplot as plt


def linear_convolution(x, h):
    N = len(x)
    z = []
    for n in range(2 * N - 2):
        sum = 0
        for k in range(N):
            if (n - k < 0) or (n - k > N - 1):
                sum += 0
            else:
                sum += x[k] * h[n - k]
        z = np.append(z, sum)
    return z


if __name__ == "__main__":
    x = np.array([4, 3, 2, 1])
    y = np.array([1, 0, -1, 0])
    z = linear_convolution(x, y)

    plt.stem(z)
    plt.show()
