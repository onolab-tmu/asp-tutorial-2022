import numpy as np
import matplotlib.pyplot as plt


def calc_vector(x, y, thete, f):
    c = 334
    assert x.shape[0] == y.shape[0], "The sizes of x and y must be equal"
    M = x.shape[0]

    u = np.array([np.sin(thete), np.cos(thete), 0])
    a = np.zeros((M)).astype(complex)
    for m in range(M):
        pm = np.array([x[m], y[m], 0]).T
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ pm)

    return a


def draw_beam_pattern(w, p, fs):
    F, M = w.shape  # 周波数ビンの総数，マイクの個数
    M, _ = p.shape  # マイクの個数，座標軸数(=2)

    a = np.zeros((M, F, 361)).astype(np.complex128)
    psi = np.zeros((F, 361)).astype(np.complex128)
    for theta in range(361):
        for f in range(F):
            a[:, f, theta] = calc_vector(p[:, 0], p[:, 1], theta, f * fs / 2 / (F - 1))
            psi[:, theta] = np.conj(w[f, :]).T @ a[:, f, theta]

    plt.pcolormesh(np.arange(361), np.arange(F), 20 * np.log10(np.abs(psi)))
    plt.xlabel("Direction [deg]")
    plt.ylabel("Freq. bins")
    plt.colorbar()
    plt.show()


fs = 16000
F = 513
M = 3
d = np.array([0.02, 0.05, 0.10])

w = np.zeros((F, 3)).astype(np.complex128)
tau = np.array([0, 10 / fs, 20 / fs])
for f in range(F):
    for i in range(3):
        w[f, i] = 1 / 3 * np.exp(-1j * 2 * np.pi * f * fs / 2 / (F - 1) * tau[i])

for i in range(3):
    p = np.zeros((M, 2))
    for m in range(M):
        p[m, :] = np.array([((m - 1) - (M - 1) / 2) * d[i], 0]).T

    plt.title(f"d = {d[i]} [m]")
    draw_beam_pattern(w, p, fs)
