import numpy as np
import matplotlib.pyplot as plt


def eq(a, b, f, fs):
    N = len(a)
    M = len(b)
    omega = 2 * np.pi * f / fs
    a_sum = 1
    b_sum = 0
    for i in range(1, N):
        a_sum += a[i] * np.exp(-1j * omega * i)
    for k in range(M):
        b_sum += b[k] * np.exp(-1j * omega * k)

    H = b_sum / a_sum

    return H


if __name__ == "__main__":
    fs = 16000
    f = np.arange(fs)/ fs

    a = [1]
    b = [0.2, 0.2, 0.2, 0.2, 0.2]

    H = eq(a, b, f, fs)

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2)
    ax1.stem(np.abs(H))
    ax2.stem(np.angle(H))
    ax1.set_title("Amplitude")
    ax2.set_title("Angle")
    fig.tight_layout()
    plt.show()
