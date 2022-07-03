import numpy as np
import matplotlib.pyplot as plt


def Hamming(N):
    n = np.arange(N)
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return win


def circular_convolution(x, h):
    N = len(x)
    z = np.zeros(N)
    for n in range(N):
        for k in range(N):
            z[n] += x[k] * h[(n - k) % N]
    return z


if __name__ == "__main__":
    A = 1
    f = 440.0
    sec = 3.0
    fs = 16000

    t = np.arange(0, sec * fs) / fs
    y = A * np.sin(2 * np.pi * f * t)

    y_npfft = np.fft.fft(y)
    X = y_npfft

    win_ham = Hamming(len(y))
    ham_dft = np.fft.fft(win_ham)
    Y = ham_dft

    N = len(y)
    n = np.arange(N)
    Z = np.zeros(N, dtype="complex")

    for k in range(N):
        Z[k] = np.sum(X[n] * Y[(k - n) % N])

    Z_i = np.fft.ifft(Z)

    y_ham = y * win_ham

    fig = plt.figure()
    fig_idft = fig.add_subplot(2, 1, 1)
    fig_ham = fig.add_subplot(2, 1, 2)
    fig_idft.plot(Z_i)
    fig_ham.plot(y_ham)
    fig.tight_layout()
    plt.show()
