import numpy as np


def synthetic_window(S, w):
    L = len(w)
    Q = int(L / S)
    w_s = np.empty(L, dtype=float)
    for i in range(0, L - 1):
        w_s[i] = 0
        for m in range(-(Q - 1), Q - 1):
            if i - m * S <= L - 1:
                w_s[i] += w[i - m * S] ** 2
        w_s[i] = w[i] / w_s[i]

    return w_s
