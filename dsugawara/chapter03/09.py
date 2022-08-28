import numpy as np
import matplotlib.pyplot as plt


def Frequency_response(a, b, f, sf):

    omega = 2 * np.pi * f / sf
    N = a.size
    M = b.size
    sigma_a = 0j
    sigma_b = 0j

    # a[N]を含むシグマ計算
    for k in range(1, N):
        sigma_a += a[k] * np.e ** (-1j * omega * k)
    # b[M]を含むシグマ計算
    for k in range(0, M):
        sigma_b += b[k] * np.e ** (-1j * omega * k)

    H = sigma_b / (1 + sigma_a)

    return H


# main
N = 16
a = np.array([1])
b = np.full(5, 0.2)
sf = 16000
H = np.zeros(N, dtype="complex")

for i in range(0, N):
    f = i / N * sf
    H[i] = Frequency_response(a, b, f, sf)


H_amp = np.abs(H)
H_angle = np.angle(H)

# plot
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.stem(H_amp)
ax2.stem(H_angle)
ax1.set_title("Amplitude characteristics")
ax2.set_title("Angle characteristics")
fig.tight_layout()
plt.savefig("09py_characteristics")
