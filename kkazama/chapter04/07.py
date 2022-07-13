import numpy as np
from matplotlib import pyplot as plt

# ゼロ詰め
def zero_pad(x, L, S):
    x = np.pad(x, (L - S, L - S))
    a = len(x) % S
    if a != 0:
        x = np.pad(x, (0, S - a))

    return x


# フレーム分割
def sep_frame(x, L, S):
    x = zero_pad(x, L, S)
    T = (len(x) - L) // S + 1
    xt = np.zeros((T, L), dtype=complex)
    for t in range(T):
        for l in range(L):
            xt[t][l] = x[t * S + l]

    return xt


# フーリエ変換
def sig_stft(x, w, L, S):
    xt = sep_frame(x, L, S)
    T = xt.shape[0]
    for t in range(T):
        xt[t] = xt[t] * w[t]

    Xk = np.fft.rfft(xt)

    return Xk


def mix_win(w, S):
    L = len(w)
    Q = L // S
    ws = np.zeros(L)
    for l in range(L):
        a = l - (Q - 1)
        if a >= 0:
            ws[l] = w[l] / np.sum(w[a:Q] ** 2)
    return ws


def istft(X, S):
    F = X.shape[0]
    T = X.shape[1]

    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x = np.zeros(M, dtype=complex)
    z = np.zeros((T, N), dtype=complex)

    w = np.hamming(S)
    w = mix_win(w, S)

    for t in range(T):
        for n in range(N):
            z[t][n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] = x[t * S + n] + w[n] * z[t][n]

    return x


A = 1
f = 440
fs = 16000
sec = 0.1
t = np.arange(0, sec * fs) / fs

x = A * np.sin(2 * np.pi * f * t)

L = 1000
w = np.hamming(L)
S = 500

Xk = sig_stft(x, w, L, S)

xt = istft(Xk, S)

plt.plot(xt)

plt.show()
