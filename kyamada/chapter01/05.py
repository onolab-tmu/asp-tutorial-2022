import numpy as np
import matplotlib.pyplot as plt


def create_white_noise(
    fs=16000,
    time=3
):
    """
    Create a white noise
    """
    t = np.arange(0, time, 1/fs)
    x = np.random.randn(len(t))
    return t, x


if __name__ == '__main__':
    np.random.seed(0)  # シード値
    t, x = create_white_noise()
    plt.plot(t, x)
    plt.show()
