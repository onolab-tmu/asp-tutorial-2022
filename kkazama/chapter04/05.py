import numpy as np


def mix_win(w, S):
    L = len(w)
    Q = L // S
    ws = np.zeros(L)
    for l in range(L):
        a = l - (Q - 1)
        if a >= 0:
            ws[l] = w[l] / np.sum(w[a:Q] ** 2)
    return ws
