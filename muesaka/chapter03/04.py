import numpy as np
import matplotlib.pyplot as plt


def linear_convolution(x, h):
    N = len(x)
    z = np.zeros(2 * N - 2)

    for n in range(2 * N - 2):
        for k in range(N):
            if (n - k >= 0) and (n - k <= N - 1):
                z[n] += x[k] * h[n - k]
    return z


def circular_convolution(x, h):
    N = len(x)
    z = np.zeros(N)

    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


def padding_circular_convolution(x_in, h):
    x = np.pad(x_in, ((0, len(x_in) - 2)))
    h = np.pad(h, ((0, len(x_in) - 2)))
    N = len(x)
    z = np.zeros(N)

    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


if __name__ == "__main__":
    x = np.array([4, 3, 2, 1])
    y = np.array([1, 0, -1, 0])

    z1 = linear_convolution(x, y)
    z2 = circular_convolution(x, y)
    z3 = padding_circular_convolution(x, y)

    fig, ax = plt.subplots(nrows=3, ncols=1)
    ax[0].stem(z1)
    ax[1].stem(z2)
    ax[2].stem(z3)
    plt.tight_layout()
    plt.show()
