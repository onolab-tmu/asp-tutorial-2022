import numpy as np
import matplotlib.pyplot as plt


def padding(L, S, x):
    zeros = np.zeros(L - S, dtype=float)
    x_pad = np.concatenate((zeros, x, zeros))
    x_pad_mod = len(x_pad) % S
    if x_pad_mod != 0:
        zeros = np.zeros(x_pad_mod, dtype=float)
        x_pad = np.concatenate((x_pad, zeros))

    return x_pad


def divide_frame(L, S, x):
    x_pad = padding(L, S, x)
    T = (len(x_pad) - L) // S + 1
    x_div = np.empty([T, L], dtype=float)
    for t in range(T):
        x_t = np.zeros(L, dtype=float)
        for i in range(L):
            if len(x_pad) > (t * S + i):
                x_t[i] = x_pad[t * S + i]
        x_div[t] = x_t

    return x_div


def stft(L, S, x):
    x_div = divide_frame(L, S, x)
    win = np.hamming(L)
    T = len(x_div)
    x_stft = np.empty([int(L / 2 + 1), T], dtype=complex)
    for t in range(T):
        x_stft[:, t] = np.fft.rfft(win * x_div[t, :])

    return x_stft


if __name__ == "__main__":
    A = 1
    f = 440
    fs = 16000
    sec = 0.1
    L = 1000
    S = 500

    t = np.arange(0, fs * sec) / fs
    x = A * np.sin(2 * np.pi * f * t)

    X = stft(L, S, x)

    fig, ax = plt.subplots(nrows=2, ncols=1)

    ax[0].pcolormesh(np.abs(X))
    ax[0].set_title("Amplitude")
    ax[1].pcolormesh(np.angle(X))
    ax[1].set_title("Phase")

    plt.tight_layout()
    plt.show()
