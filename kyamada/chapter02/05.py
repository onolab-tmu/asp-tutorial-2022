import numpy as np
import matplotlib.pyplot as plt


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
    t = np.arange(0, fs*time) / fs
    x = r * np.sin(2 * np.pi * f * t + theta)

    return t, x


def dft(x):
    """
    DFT
    Input:
        x: input array
    Output:
        X: output DFT array
    """
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp((-2j * np.pi * k * n) / N)
    return X


if __name__ == '__main__':
    fs = 16000
    t, x = create_sinusoid(fs=fs)

    X = dft(x)

    X_amp = 20 * np.log10(np.abs(X))
    X_phase = 20 * np.log10(np.angle(X))
    plt.subplot(2, 1, 1)
    plt.stem(X_amp)
    plt.grid()
    plt.title("Amplitude")
    plt.subplot(2, 1, 2)
    plt.stem(X_phase)
    plt.grid()
    plt.title("Phase")
    plt.show()
