import numpy as np


def zero_pad(L, S, x):
    zeros = np.zeros(L - S)
    x_pad = np.concatenate((zeros, x, zeros))
    x_smod = len(x_pad) % S
    if x_smod != 0:
        zeros_smod = np.zeros(x_smod)
        x_pad = np.concatenate((x_pad, zeros_smod))

    return x_pad


if __name__ == "__main__":
    N = 3
    L = 4
    S = 2
    x = np.arange(N)
    x_zero = zero_pad(L, S, x)
    print(x)
    print(x_zero)
