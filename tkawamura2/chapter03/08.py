import numpy as np


def freq_res(y, a, b, fs):
    omega = np.arange(0, fs)/fs
    F = omega.size
    N = a.size
    M = b.size
    H = np.zeros(F)

    for o, f in enumerate(omega):
        a_sum = 1
        b_sum = 0
        for k1 in np.arange(1, N):
            a_sum = a_sum + a[k1]*np.exp(-1j*o*k1)
        for k2 in range(M):
            b_sum = b_sum + b[k2]*np.exp(-1j*o*k2)
        H[f] = b_sum/a_sum
    return H
