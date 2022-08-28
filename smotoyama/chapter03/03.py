import numpy as np


def linear_conv_cir(x, h):
    N = len(x)
    x = np.pad(x, [0, N - 2])
    h = np.pad(h, [0, N - 2])
    z = np.zeros(2 * N - 2)
    for n in range(z.size):
        for k in range(z.size):
            z[n] += x[k] * h[(n - k) % z.size]
    return z


def linear_conv(x, h):
    N = len(x)
    z = np.zeros(2 * N - 2)
    for n in range(z.size):
        for k in range(N):
            if n - k >= 0 and n - k <= N - 1:
                z[n] += x[k] * h[n - k]
    return z


if __name__ == "__main__":
    x = [4, 3, 2, 1]
    y = [1, 0, -1, 0]

    z_lin = linear_conv(x, y)
    z_cir = linear_conv_cir(x, y)

    print(z_lin, z_cir)
