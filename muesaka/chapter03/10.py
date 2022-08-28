import numpy as np
import matplotlib.pyplot as plt


def calculate_frequency_responce(a, b, f, fs):
    N = len(a)
    M = len(b)
    tmp_a = 0
    tmp_b = 0
    omega = 2 * np.pi * f / fs

    for k in range(0, M):
        tmp_b += b[k] * np.exp(-1j * omega * k)
    for k in range(1, N):
        tmp_a += a[k] * np.exp(-1j * omega * k)
    H = tmp_b / (1 + tmp_a)

    return H


if __name__ == "__main__":
    a = np.array([1, -0.3])
    b = np.array([0.4])
    N = 16
    H = np.zeros(N, dtype="complex")
    fs = 16000
    f = np.zeros(N)

    for i in range(N):
        f[i] = i * fs / N
        H[i] = calculate_frequency_responce(a, b, f[i], fs)

    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].stem(f, np.abs(H))
    ax[1].stem(f, np.angle(H))
    plt.tight_layout()
    plt.show()
