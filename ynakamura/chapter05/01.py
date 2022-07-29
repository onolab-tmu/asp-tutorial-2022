import numpy as np


def calc_linear_vector(d, M, thete, f):
    c = 334

    u = np.array([np.sin(thete), np.cos(thete), 0])
    a = np.zeros((M)).astype(complex)
    for m in range(M):
        pm = np.array([((m - 1) - (M - 1) / 2) * d, 0, 0]).T
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ pm)

    return a


print(calc_linear_vector(0.05, 3, 45, 1000))
