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
def sig_stft(x, L, S):
    xt = sep_frame(x, L, S)
    w = np.hamming(L)
    T = xt.shape[0]
    X = np.zeros((L // 2 + 1, T), dtype=complex)
    for t in range(T):
        xt[t] = xt[t] * w
        X[:, t] = np.fft.rfft(xt[t])

    return X


A = 1
f = 440
fs = 16000
sec = 1

t = np.arange(0, sec * fs) / fs

x = A * np.sin(2 * np.pi * f * t)

L = np.array([100, 200, 400, 800])

for i in range(L.size):
    S = L[i] // 2
    Xk = sig_stft(x, L[i], S)
    X, Y = np.mgrid[: Xk.shape[1] + 1, : Xk.shape[0] + 1]
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pcolormesh(X, Y, 20 * np.log10(np.abs(Xk)).T)

    plt.show()
