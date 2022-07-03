import numpy as np


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

    print(circular_convolution(x, y))
