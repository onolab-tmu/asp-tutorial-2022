import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    N = 10
    x = np.zeros(N + 4)
    x[4] = 1
    y = np.zeros(N)
    for n in range(N):
        y[n] = (
            0.2 * x[n + 4]
            + 0.2 * x[n + 3]
            + 0.2 * x[n + 2]
            + 0.2 * x[n + 1]
            + 0.2 * x[n]
        )

    plt.stem(y)
    plt.show()
