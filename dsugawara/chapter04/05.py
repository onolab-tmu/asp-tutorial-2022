import numpy as np


def optimal_window(S, win):

    L = win.size
    Q = L // S
    for l in range(0, L):
        sigma = 0
        for m in range(0, Q):
            sigma += win[l - m * S] ** 2
    win_s = win / sigma

    return win_s
