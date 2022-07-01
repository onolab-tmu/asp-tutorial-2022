import numpy as np
import matplotlib.pyplot as plt


def linear_convolution(x, h):
    K = len(x)
    z = np.zeros(2 * K - 2)
    for n in range(2 * K - 2):
        for k in range(K):
            if n - k >= 0 and n - k <= K - 1:
                z[n] += x[k] * h[n - k]
    return z


def circular_convolution(x, h):
    N = len(x)
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


if __name__ == "__main__":
    x = [4, 3, 2, 1]
    y = [1, 0, -1, 0]
    N = len(x)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax1.stem(linear_convolution(x, y), label="linear")
    ax2.stem(circular_convolution(x, y), label="circular")
    ax3.stem(circular_convolution(np.pad(x, ((0, N - 2))), np.pad(y, ((0, N - 2)))))
    ax1.set_title("linear")
    ax2.set_title("circular")
    ax3.set_title("padded circular")
    plt.tight_layout()
    plt.show()
