import numpy as np
import matplotlib.pyplot as plt


def linear_conv(x, h):
    N = len(x)
    z = np.zeros(2 * N - 2)
    for n in range(z.size):
        for k in range(N):
            if n - k >= 0 and n - k <= N - 1:
                z[n] += x[k] * h[n - k]
    return z


def circular_conv(x, h):
    N = len(x)
    z = np.zeros(N)
    for n in range(z.size):
        for k in range(z.size):
            z[n] += x[k] * h[(n - k) % N]
    return z


def linear_conv_cir(x, h):
    N = len(x)
    x = np.pad(x, [0, N - 2])
    h = np.pad(h, [0, N - 2])
    z = np.zeros(2 * N - 2)
    for n in range(z.size):
        for k in range(z.size):
            z[n] += x[k] * h[(n - k) % z.size]
    return z


if __name__ == "__main__":
    x = [4, 3, 2, 1]
    y = [1, 0, -1, 0]
    N = len(x)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax1.stem(linear_conv(x, y), label="linear")
    ax2.stem(circular_conv(x, y), label="circular")
    ax3.stem(linear_conv_cir(x, y), label="0_pad")
    ax1.set_title("linear")
    ax2.set_title("circular")
    ax3.set_title("0 padded")
    plt.tight_layout()
    plt.show()
