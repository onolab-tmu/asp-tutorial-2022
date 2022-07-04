import numpy as np


def pad(x, L, S):
    x_ = np.pad(x, [L - S, L - S])
    a = np.mod(x_.size, S)
    if a != 0:
        x_ = np.pad(x_, [0, S - a])
    return x_
