import numpy as np
import matplotlib.pyplot as plt


def eq(x):
    N = len(x)
    y = np.zeros(N)
    for i in range(N):
        if i - 1 < 0:
            y[i] = 0.4 * x[i]
        else:
            y[i] = 0.3 * y[i - 1] + 0.4 * x[i]
    return y


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1

    plt.stem(eq(x))
    plt.show()
