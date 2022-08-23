import numpy as np
import matplotlib.pyplot as plt


def calc_vector(crd, theta, f):
    M = crd.shape[1]
    x = crd[0]
    y = crd[1]
    if len(x) != len(y):
        print("Error: The numbers x and y are not equal.")
        exit()
    c = 334
    u = np.array([np.sin(theta), np.cos(theta), 0]).T
    a = np.zeros(M, dtype="complex")
    for m in range(M):
        p_m = np.array([x[m], y[m], 0]).T
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ p_m)

    return a


def plot_beam_pattern(w, p, sr):
    F, M = w.shape
    M = p.shape[0]

    crd = np.zeros((3, M))
    for m in range(M):
        crd[0][m] = p[m][0]

    a = np.zeros((M, F, 361), dtype="complex")
    psi = np.zeros((F, 361), dtype="complex")
    for theta in range(361):
        for f in range(F):
            a[:, f, theta] = calc_vector(crd, theta, f * sr / 2 / (F - 1))
            psi[:, theta] = np.conj(w[f]).T @ a[:, f, theta]

    plt.pcolormesh(np.arange(361), np.arange(F), 20 * np.log10(np.abs(psi)))
    plt.xlabel("angle [deg]")
    plt.ylabel("frequency [Hz]")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig("outputs/08.pdf")
    plt.show()


sr = 16000
d = 0.05
M = 3
L = 1024
F = L // 2 + 1

tau = np.array([0, 10 / sr, 20 / sr])
w = np.zeros((F, M), dtype="complex")
for f in range(F):
    for m in range(M):
        w[f, m] = 1 / M * np.exp(-1j * 2 * np.pi * f * sr / 2 / (F - 1) * tau[m])

p = np.zeros((M, 3))
for m in range(M):
    p[m] = np.array([((m - 1) - (M - 1) / 2) * d, 0, 0]).T

plot_beam_pattern(w, p, sr)

print("success!")
