import numpy as np


def circ_amvector(r, M, theta, f):
    c = 334  # 音速

    p = 2 * np.pi / M * np.arange(M)
    p_1 = r * np.sin(p)
    p_1 = p_1.reshape([1, p_1.size])
    p_2 = r * np.cos(p)
    p_2 = p_2.reshape([1, p_2.size])
    zero = np.zeros(p.size)
    zero = zero.reshape([1, zero.size])
    p_m = np.concatenate([p_1, p_2, zero]).T

    u = np.array([np.sin(theta), np.cos(theta), 0])

    tmp = 2 * np.pi * f / c * u * p_m
    return np.exp(tmp*1j)


print(circ_amvector(0.05, 3, np.pi/4, 1000))
