import numpy as np


def syn_win(win, S):
    L = win.size
    Q = int(np.floor(L / S))
    swin = np.empty(L, dtype=np.float64)
    for i in range(L):
        k = i - (Q - 1) * S
        if k < 0:
            k = 0
        swin[i] = win[i] / np.sum(win[k: i + (Q - 1) * S]**2)
    return swin
