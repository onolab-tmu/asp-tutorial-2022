import numpy as np
import matplotlib.pyplot as plt


def Myhamming(N):
    """
    My hamming window
    Input:
        x: input array
    Output:
        x: output array
    """
    n = np.arange(N)
    # for n in range(N):
    win = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N-1))
    return win


if __name__ == '__main__':

    x = Myhamming(16000)
    plt.plot(x)
    plt.grid()
    plt.show()
