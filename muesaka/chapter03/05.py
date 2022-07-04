import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    N = len(x)
    y = np.zeros(N)

    for n in range(N):
        for k in range(5):
            if (k <= n) and (n - k <= 4):
                y[n] = 0.2 * x[n - k]

    plt.stem(y)
    plt.tight_layout()
    plt.show()
