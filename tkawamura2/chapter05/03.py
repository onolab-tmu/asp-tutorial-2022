import numpy as np


def amvector(mic_arg, theta, f):
    c = 334  # 音速

    u = np.array([np.sin(theta), np.cos(theta), 0])

    tmp = 2 * np.pi * f / c * u * mic_arg
    return np.exp(tmp*1j)


d = 0.05
M = 3

p = (np.arange(M) - (M - 1) / 2) * d
p = p.reshape([1, p.size])
zero = np.zeros(p.size)
zero = zero.reshape([1, zero.size])
p_m = np.concatenate([p, zero, zero]).T
print(amvector(p_m, np.pi/4, 1000))

r = 0.05

p = 2 * np.pi / M * np.arange(M)
p_1 = r * np.sin(p)
p_1 = p_1.reshape([1, p_1.size])
p_2 = r * np.cos(p)
p_2 = p_2.reshape([1, p_2.size])
zero = np.zeros(p.size)
zero = zero.reshape([1, zero.size])
p_m = np.concatenate([p_1, p_2, zero]).T
print(amvector(p_m, np.pi/4, 1000))
