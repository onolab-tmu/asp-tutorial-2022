import numpy as np
import matplotlib.pyplot as plt


def difference_equation_05(x):
    """
    Input
        x : input signal
    Output
        y: output signal
    """
    y = 0.2 * x[0:-4] + 0.2 * x[1:-3] + 0.2 * \
        x[2:-2] + 0.2 * x[3:-1] + 0.2 * x[4:]
    return y


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1

    y = difference_equation_05(x)
    print(y)

    plt.stem(y)
    plt.show()
