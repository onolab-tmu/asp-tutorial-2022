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


def plot_beam_pattern(w, p, sr, d):
    F, M = w.shape
    M = p.shape[0]

    crd_lin = np.zeros((3, M))
    for m in range(M):
        crd_lin[0][m] = p[m][0]

    a_lin = np.zeros((M, F, 361), dtype="complex")
    psi = np.zeros((F, 361), dtype="complex")
    for theta in range(361):
        for f in range(F):
            a_lin[:, f, theta] = calc_vector(crd_lin, theta, f * sr / 2 / (F - 1))
            psi[:, theta] = np.conj(w[f]).T @ a_lin[:, f, theta]

    plt.pcolormesh(np.arange(361), np.arange(F), 20 * np.log10(np.abs(psi)))
    plt.xlabel("angle [deg]")
    plt.ylabel("frequency [Hz]")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(f"outputs/09_{d}.pdf")
    plt.show()
    plt.clf()
    plt.close()


sr = 16000
d = [0.02, 0.05, 0.07]
d_length = len(d)
M = 3
L = 1024
F = L // 2 + 1

tau = np.array([0, 10 / sr, 20 / sr])
w = np.zeros((F, M), dtype="complex")
for f in range(F):
    for m in range(M):
        w[f, m] = 1 / M * np.exp(-1j * 2 * np.pi * f * sr / 2 / (F - 1) * tau[m])

p = np.zeros((d_length, M, 3))
for i in range(d_length):
    for m in range(M):
        p[i, m, :] = np.array([((m - 1) - (M - 1) / 2) * d[i], 0, 0]).T

for i in range(d_length):
    plot_beam_pattern(w, p[i], sr, d[i])

print("success!")
