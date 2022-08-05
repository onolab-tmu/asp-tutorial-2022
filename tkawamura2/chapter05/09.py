import numpy as np
# from math import ceil
import matplotlib.pyplot as plt


def amvector(mic_arg, theta, f):
    c = 334  # 音速

    u = np.array([np.sin(theta), np.cos(theta), 0])

    tmp = 2 * np.pi * f / c * u * mic_arg
    return np.exp(tmp*1j)


def beam_pattern(w, mic_arg, fs):
    F = w.shape[0]
    # f = np.arange(ceil(fs / (2 * F - 1)))
    f = np.arange(F)
    theta = np.arange(360)
    Psi = np.empty([f.size, theta.size], dtype=np.complex128)

    for f_ in f:
        for t in theta:
            Psi[f_, t] = np.conj(w[f_]).T @ amvector(mic_arg, t, f_)[0]

    fig, ax = plt.subplots(figsize=(5, 5))
    bp = ax.pcolormesh(theta, f, 20 * np.log10(np.abs(Psi)), cmap="magma")
    fig.colorbar(bp, ax=ax, orientation="vertical")
    plt.show()


d = np.array([0.02, 0.05, 0.1])
M = 3
fs = 16000
F = 512

for d_ in d:
    p = (np.arange(M) - (M - 1) / 2) * d_
    p = p.reshape([1, p.size])
    zero = np.zeros(p.size)
    zero = zero.reshape([1, zero.size])
    p_m = np.concatenate([p, zero, zero]).T

    w = np.empty([F, 3], dtype=np.complex128)
    for j in range(F):
        w[j] = np.array([np.exp(-2j * np.pi * j * 0),
                         np.exp(-2j * np.pi * j * 10 / fs),
                         np.exp(-2j * np.pi * j * 20 / fs)]) / 3

    beam_pattern(w, p_m, fs)
