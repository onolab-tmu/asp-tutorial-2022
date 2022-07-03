import numpy as np
import matplotlib.pyplot as plt


def DFT(x):
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N)
    for k in range(N):
        X[k] = np.sum(x * np.exp(-1j * 2 * np.pi * k * n / N))
    return X


def IDFT(X):
    N = len(X)
    k = np.arange(N)
    x = np.zeros(N)
    for n in range(N):
        x[n] = np.sum(X * np.exp(1j * 2 * np.pi * k * n / N)) / N
    return x


if __name__ == "__main__":
    delta = [1, 0, 0, 0, 0, 0, 0, 0]
    delta_dft = DFT(delta)
    delta_idft = IDFT(delta_dft)

    delta_amp = np.abs(delta_idft)
    delta_angle = np.angle(delta_idft)

    fig = plt.figure()
    fig_amp = fig.add_subplot(2, 1, 1)
    fig_angle = fig.add_subplot(2, 1, 2)
    fig_amp.stem(delta_amp)
    fig_angle.stem(delta_angle)
    fig_amp.set_title("Amplitude")
    fig_angle.set_title("Angle")
    fig.tight_layout()
    plt.show()
