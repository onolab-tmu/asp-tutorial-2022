import numpy as np


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


# 1.の問題設定
x_1 = np.array([0.1, 0.05, 0.0])
y_1 = np.array([0, 0, 0])
print(calc_vector(x_1, y_1, 45, 1000))

# 2.の問題設定
x_2 = np.array([-0.0433, 0, 0.0433])
y_2 = np.array([-0.025, 0.05, -0.025])
print(calc_vector(x_2, y_2, 45, 1000))
