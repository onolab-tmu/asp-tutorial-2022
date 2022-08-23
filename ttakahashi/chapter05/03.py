import numpy as np


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


d = 0.05
r = 0.05
M = 3
theta = 45
f = 1000
crd_lin = np.zeros((3, M))
crd_cir = np.zeros((3, M))

for m in range(M):
    crd_lin[0][m] = ((m - 1) - (M - 1) / 2) * d
    crd_cir[0][m] = r * np.sin(2 * np.pi / M * (m - 1))
    crd_cir[1][m] = r * np.cos(2 * np.pi / M * (m - 1))

a_lin = calc_vector(crd_lin, theta, f)
a_cir = calc_vector(crd_cir, theta, f)
print("Linear: " + str(a_lin))
print("Circular: " + str(a_cir))

print("success!")
