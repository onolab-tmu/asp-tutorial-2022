import numpy as np
import matplotlib.pyplot as plt


def Myhamming(x):
    """
    My hamming window
    Input:
        x: input array
    Output:
        x: output array
    """
    N = len(x)
    x = np.zeros(len(x))
    for n in range(N):
        x[n] = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return x


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
    fs = 16000
    t, x = create_sinusoid(fs=fs)
    wind = Myhamming(x)
    x = x * wind
    X = np.fft.fft(x)
    plt.subplot(2, 1, 1)
    plt.stem(X.real)
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.stem(X.imag)
    plt.grid()
    plt.show()

