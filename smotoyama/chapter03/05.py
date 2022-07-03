import numpy as np
import matplotlib.pyplot as plt


def eq(x):
    N = len(x)
    y = np.zeros(N)
    for i in range(N):
        y[i] = (
            0.2 * x[i]
            + 0.2 * x[i - 1]
            + 0.2 * x[i - 2]
            + 0.2 * x[i - 3]
            + 0.2 * x[i - 4]
        )
    return y


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1

    plt.stem(eq(x))
    plt.show()
