import numpy as np


def liner_amvector(d, M, theta, f):
    c = 334  # 音速

    p = (np.arange(M) - (M - 1) / 2) * d
    p = p.reshape([1, p.size])
    zero = np.zeros(p.size)
    zero = zero.reshape([1, zero.size])
    p_m = np.concatenate([p, zero, zero]).T

    u = np.array([np.sin(theta), np.cos(theta), 0])

    tmp = 2 * np.pi * f / c * u * p_m
    return np.exp(tmp*1j)


print(liner_amvector(0.05, 3, np.pi/4, 1000))
