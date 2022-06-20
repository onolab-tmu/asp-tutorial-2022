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


def create_sinusoid(
    fs=16000,
    f=440,
    r=1,
    theta=0,
    time=3,
):
    """
    Create a sinusoid wave
    Input:
        fs: sampling frequency
        f: frequency
        r: amplitude
        theta: phase
        time: time
    Output:
        t: time_data
        x: wave data
    """
    t = np.arange(0, time, 1/fs)
    x = r * np.sin(2 * np.pi * f * t + theta)

    return t, x


if __name__ == '__main__':
    np.random.seed(0)  # シード値
    t, noise = create_white_noise()
    t, x_sinusoid = create_sinusoid()
    x = noise + x_sinusoid
    plt.plot(t, x)
    plt.show()
