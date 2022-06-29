import numpy as np
import matplotlib.pyplot as plt


def calculate_difference(x):
    z = []
    for n in range(len(x)):
        sum = 0
        for k in range(5):
            if n - k < 0:
                sum += 0
            else:
                sum += x[n - k]
        z = np.append(z, sum)
    return z


if __name__ == "__main__":
    x = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    z = calculate_difference(x)

    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].stem(x)
    ax[1].stem(z)
    plt.tight_layout()
    plt.show()
