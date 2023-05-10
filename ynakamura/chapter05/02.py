import numpy as np


def calc_circular_vector(r, M, thete, f):
    c = 334

    u = np.array([np.sin(thete), np.cos(thete), 0])
    a = np.zeros((M)).astype(complex)
    for m in range(M):
        pm = np.array(
            [
                r * np.sin(2 * np.pi / M * (m - 1)),
                r * np.cos(2 * np.pi / M * (m - 1)),
                0,
            ]
        ).T
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ pm)

    return a


print(calc_circular_vector(0.05, 3, 45, 1000))
