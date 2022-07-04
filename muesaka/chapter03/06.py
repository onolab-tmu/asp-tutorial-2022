import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    N = len(x)
    y = np.zeros(N)

    for n in range(N):
        if n == 0:
            y[n] = 0.4 * x[n]
        else:
            y[n] = 0.3 * y[n - 1] + 0.4 * x[n]

    plt.stem(y)
    plt.tight_layout()
    plt.show()
