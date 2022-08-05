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


def synthetic_window(S, w):
    L = len(w)
    Q = int(L / S)
    w_s = np.empty(L, dtype=float)
    for i in range(L):
        w_s[i] = 0
        for m in range(-(Q - 1), Q):
            if i - m * S < L:
                w_s[i] += w[i - m * S] ** 2
        w_s[i] = w[i] / w_s[i]
    return w_s


def istft(S, X):
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x_hat = np.zeros(M, dtype=complex)
    z = np.zeros((T, N), dtype=complex)
    w = np.hamming(N)
    w_s = synthetic_window(S, w)

    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x_hat[t * S + n] = x_hat[t * S + n] + w_s[n] * z[t, n]

    return x_hat


def istft_ones(S, X):
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    x_hat = np.zeros(M, dtype=complex)
    z = np.zeros((T, N), dtype=complex)
    w_s = np.ones(N, dtype=float)

    for t in range(T):
        for n in range(N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x_hat[t * S + n] = x_hat[t * S + n] + w_s[n] * z[t, n]

    return x_hat


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
    x_hat = istft(S, X)
    x_ones = istft_ones(S, X)

    fig, ax = plt.subplots(nrows=2, ncols=1)

    ax[0].plot(x_hat)
    ax[0].set_title("w_s = hamming")
    ax[1].plot(x_ones)
    ax[1].set_title("w_s = ones")

    plt.tight_layout()
    plt.show()
