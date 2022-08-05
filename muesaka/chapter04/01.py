import numpy as np


def padding(L, S, x):
    zeros = np.zeros(L - S, dtype=float)
    x_pad = np.concatenate((zeros, x, zeros))
    x_pad_mod = len(x_pad) % S
    if x_pad_mod != 0:
        zeros = np.zeros(x_pad_mod, dtype=float)
        x_pad = np.concatenate((x_pad, zeros))

    return x_pad
