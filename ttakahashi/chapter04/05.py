import numpy as np


def syn_wnd(wnd, S):
    L = len(wnd)
    Q = L // S
    swnd = np.zeros(L)
    for i in range(L):
        k = i - (Q - 1) * S
        if k < 0:
            k = 0
        swnd[i] = wnd[i] / np.sum(wnd[k : i + (Q - 1) * S] ** 2)
    return swnd
