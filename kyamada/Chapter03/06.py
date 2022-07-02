import numpy as np
import matplotlib.pyplot as plt


def y_recursive(x):
    y = np.zeros_like(x)
    y[0] = 0.4 * x[0]
    for i in range(1, x.size):
        y[i] = 0.3 * y[i-1] + 0.4 * x[i]
    return y


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1
    y = y_recursive(x)
    print(y)

    plt.stem(y)
    plt.grid()
    plt.show()
