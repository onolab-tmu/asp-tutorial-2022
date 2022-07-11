import numpy as np
import math


def zero_pad(L, S, x):
    zeros = np.zeros(L - S)
    x_pad = np.concatenate((zeros, x, zeros))
    x_smod = len(x_pad) % S
    if x_smod != 0:
        zeros_smod = np.zeros(x_smod)
        x_pad = np.concatenate((x_pad, zeros_smod)).astype(np.int64)

    return x_pad


def divide_frame(L, S, x):
    x_pad = zero_pad(L, S, x)
    T = math.floor((len(x_pad) - L) / S) + 1
    x_div = np.empty([T, L])
    for t in range(T):
        x_t = np.zeros(L)
        for i in range(L):
            if len(x_pad) > (t * S + i):
                x_t[i] = x_pad[t * S + i]
        x_div[t] = x_t
    #        x_div = np.append(x_div, x_t)

    return x_div


if __name__ == "__main__":
    N = 3
    L = 4
    S = 2
    x = np.arange(N)

    x_pad_1 = zero_pad(L, S, x)
    x_div_1 = divide_frame(L, S, x)

    print(x_pad_1)
    print(x_div_1)
