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
    t = np.arange(0, time, 1/fs)
    x = r * np.sin(2 * np.pi * f * t + theta)

    return t, x





if __name__ == '__main__':
    fs = 16000
    t, x = create_sinusoid(fs=fs)
    print(int(0.003*fs))
    plt.plot(t, x)
    plt.xlim([0, 0.03])
    plt.show()

    
