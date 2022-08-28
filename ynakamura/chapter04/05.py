import numpy as np


def composite_win(S, win):
    L = win.shape[0]
    Q = L // S
    for nL in range(L):
        sum = 0
        for nQ in range(Q):
            sum += win[nL - nQ * S] ** 2
    win_s = win / sum
    return np.array(win_s)
