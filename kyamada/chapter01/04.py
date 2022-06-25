import numpy as np
import matplotlib.pyplot as plt
import wave


def create_two_sinusoid(
    fs=16000,
    f1=440,
    r1=1,
    theta1=0,
    f2=660,
    r2=1,
    theta2=0,
    time=3,
):
    """
    Create a sinusoid wave
    Input:
        fs: sampling frequency
        f1: frequency
        r1: amplitude
        theta1: phase
        f2: frequency
        r2: amplitude
        theta2: phase
        time: time
    Output:
        t: time_data
        x: wave data
    """
    t = np.arange(0, time, 1/fs)
    x = r1 * np.sin(2 * np.pi * f1 * t + theta1) + r2 * \
        np.sin(2 * np.pi * f2 * t + theta2)

    return t, x


def save_wave_file_2ch(filename, framerate, x):
    """
    Save a wave file
    Input:
        filename: wave file name
        x: wave data
    """
    wf = wave.open(f'{filename}.wav', 'w')
    wf.setnchannels(2)
    wf.setsampwidth(2)
    wf.setframerate(framerate)
    wf.writeframes(x.astype(np.int16).tostring())
    wf.close()


if __name__ == '__main__':
    t, x = create_two_sinusoid(r1=1000,r2=1000)
    # save wave file
    save_wave_file_2ch('kyamada/chapter01/sinusoid_2ch', 16000, x)
    plt.plot(t, x)
    plt.show()
