import numpy as np
import math
import matplotlib.pyplot as plt


def zero_pad(L, S, x):
    zeros = np.zeros(L - S)
    x_pad = np.concatenate((zeros, x, zeros))
    x_smod = len(x_pad) % S
    if x_smod != 0:
        zeros_smod = np.zeros(x_smod)
        x_pad = np.concatenate((x_pad, zeros_smod)).astype(np.int64)

    return x_pad


def divide_frame(L, S, x):
    x_pad = zero_pad(L, S, x)
    T = math.floor((len(x_pad) - L) / S) + 1
    x_div = np.empty([T, L])
    for t in range(T):
        x_t = np.zeros(L)
        for i in range(L):
            if len(x_pad) > (t * S + i):
                x_t[i] = x_pad[t * S + i]
        x_div[t] = x_t
    #        x_div = np.append(x_div, x_t)

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

    x_pad_1 = zero_pad(L, S, x)
    x_div_1 = divide_frame(L, S, x)
    x_stft_1 = stft(L, S, x)

    """
    X, Y = np.mgrid[: x_stft_1.shape[1], : x_stft_1.shape[0]]
    C = x_stft_1
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pcolormesh(X, Y, C)
    plt.show()
    """
    C = stft(L, S, x)
    X, Y = np.mgrid[: C.shape[1] + 1, : C.shape[0] + 1]
    fig, ax = plt.subplots(figsize=(5, 5))
    spec = ax.pcolormesh(X, Y, 20 * np.log10(np.abs(C)).T, cmap="magma")
    cb = fig.colorbar(spec, ax=ax, orientation="vertical")

    plt.show()
