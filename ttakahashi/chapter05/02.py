import numpy as np


def calc_circular_vector(r, M, theta, f):
    c = 334
    u = np.array([np.sin(theta), np.cos(theta), 0]).T
    a = np.zeros(M, dtype="complex")
    for m in range(M):
        p_m = np.array([r * np.sin(2 * np.pi / M * (m - 1)), r * np.cos(2 * np.pi / M * (m - 1)), 0]).T
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ p_m)

    return a


r = 0.05
M = 3
theta = 45
f = 1000
a = calc_circular_vector(r, M, theta, f)
print(a)

print("success!")
