import numpy as np
import scipy.signal as sp
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
    fs = 16000
    sec = 1
    fmin = 100
    fmax = 16000
    L = [100, 200, 400, 800]
    S = [50, 100, 200, 400]

    t = np.arange(0, fs * sec) / fs
    x_chirp = sp.chirp(t, fmin, sec, fmax)

    fig, ax = plt.subplots(nrows=2, ncols=2)
    i = 0
    for j in range(2):
        for k in range(2):
            X = stft(L[i], S[i], x_chirp)
            ax[j, k].pcolormesh(20 * np.log10(np.abs(X)))
            ax[j, k].set_title(str(L[i]) + "/" + str(S[i]))
            i += 1

    plt.tight_layout()
    plt.show()
