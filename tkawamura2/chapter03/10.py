import numpy as np
import matplotlib.pyplot as plt


def freq_res(a, b, fs):
    omega = np.arange(0, fs)/fs
    F = omega.size
    N = a.size
    M = b.size
    H = np.zeros(F, dtype=np.complex128)

    for f, o in enumerate(omega):
        a_sum = 1 + 0j
        b_sum = 0 + 0j
        for k1 in np.arange(1, N):
            a_sum = a_sum + a[k1]*np.exp(-1j*o*k1)
        for k2 in range(M):
            b_sum = b_sum + b[k2]*np.exp(-1j*o*k2)
        H[f] = b_sum/a_sum
    return H


fs = 16000
b = np.array([0.4, 0], dtype=np.complex128)
a = np.array([0, 0.3], dtype=np.complex128)

H = freq_res(a, b, fs)

plt.plot(np.abs(H))
# plt.plot(20*np.log10(np.abs(H)))
plt.show()

plt.plot(np.angle(H))
# plt.plot(20*np.log10(np.angle(H)))
plt.show()
