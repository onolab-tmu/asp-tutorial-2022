import numpy as np
import matplotlib.pyplot as plt


def zero_padding(x, h):
    x = np.pad(x, (x.size // 2, x.size // 2 - 1))
    h = np.pad(h, (h.size // 2, h.size // 2 - 1))
    return x, h


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
    z1 = linear_convolution(x, y)
    z2 = circular_convolution(x, y)
    x, y = zero_padding(x, y)
    z3 = circular_convolution(x, y)

    fig, ax = plt.subplots(nrows=3, ncols=1)
    ax[0].stem(z1)
    ax[1].stem(z2)
    ax[2].stem(z3)
    plt.tight_layout()
    plt.show()
