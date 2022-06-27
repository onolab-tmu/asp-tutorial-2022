import numpy as np
import matplotlib.pyplot as plt


def difference_equation(a, b, x, plots):
    N = len(a)
    M = len(b)
    X = len(x)
    y = np.zeros(plots)

    for p in range(plots):
        tmpa = 0
        tmpb = 0
        for n in range(1, N):
            if p - n >= 0:
                tmpa += a[n] * y[p - n]
        for m in range(M):
            if p - m >= 0 and p - m < X:
                tmpb += b[m] * x[p - m]
        y[p] = -tmpa + tmpb

    y /= a[0]
    return y


if __name__ == "__main__":
    a = [1, -0.3]
    b = [0.4]
    x = [1]

    y = difference_equation(a, b, x, 10)

    plt.stem(y)
    plt.show()
