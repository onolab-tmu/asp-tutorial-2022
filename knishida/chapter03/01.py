import numpy as np


def linear_convolution(x, h):
    K = len(x)
    z = np.zeros(2 * K - 2)
    for n in range(2 * K - 2):
        for k in range(K):
            if n - k >= 0 and n - k <= K - 1:
                z[n] += x[k] * h[n - k]
    return z


if __name__ == "__main__":
    x = [4, 3, 2, 1]
    y = [1, 0, -1, 0]

    print(linear_convolution(x, y))
