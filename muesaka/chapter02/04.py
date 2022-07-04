import numpy as np
import matplotlib.pyplot as plt


def dft(x):
    N = len(x)
    n = np.arange(N)
    dft_x = np.zeros(N, dtype=complex)
    for k in range(N):
        dft_x[k] = np.sum(x[n] * np.exp(-1j * 2 * np.pi * k * n / N))
    return dft_x


if __name__ == "__main__":
    delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])  # インパルス信号

    dft_delta = dft(delta)
    amp_dft_delta = np.abs(dft_delta)
    phase_dft_delta = np.angle(dft_delta)

    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].stem(amp_dft_delta)
    ax[0].set_title("amplitude")
    ax[1].stem(phase_dft_delta)
    ax[1].set_title("phase")
    plt.tight_layout()
    plt.show()
