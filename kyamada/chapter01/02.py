import numpy as np
import wave


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


def save_wave_file(filename, framerate, x):
    """
    Save a wave file
    Input:
        filename: wave file name
        x: wave data
    """
    wf = wave.open(f'{filename}.wav', 'w')
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(framerate)
    wf.writeframes(x.astype(np.int16).tostring())
    wf.close()


if __name__ == '__main__':
    t, x = create_sinusoid(r=1000)
    # save wave file
    save_wave_file('kyamada/chapter01/sinusoid', 16000, x)
