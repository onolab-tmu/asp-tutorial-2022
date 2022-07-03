import numpy as np
import matplotlib.pyplot as plt


def frequency_responce(a, b, f, fs):
    N = len(a)
    M = len(b)
    tmpa = 0
    tmpb = 0
    omega = 2 * np.pi * f / fs
    for k in range(1, N):
        tmpa += a[k] * np.exp(-1j * omega * k)
    for k in range(M):
        tmpb += b[k] * np.exp(-1j * omega * k)
    H = tmpb / (1 + tmpa)
    return H


if __name__ == "__main__":
    a = [1, 0.3]
    b = [0.4]
    fs = 16000
    N = 16
    H = np.zeros(N)
    f = 0

    for i in range(N):
        f = i / N * fs
        H[i] = frequency_responce(a, b, f, fs)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.stem(np.abs(H))
    ax2.stem(np.angle(H))
    ax1.set_title("Amplitude")
    ax2.set_title("Angle")
    fig.tight_layout()
    plt.show()
