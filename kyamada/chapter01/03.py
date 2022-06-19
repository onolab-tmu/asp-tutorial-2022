import numpy as np
import matplotlib.pyplot as plt
import wave


def read_wave(filename, framerate=8000):
    """
    Read a wave file
    Input:
        filename: wave file name
    Output:
        fs: sampling frequency
        x: wave data
    """
    wf = wave.open(filename, 'r')
    fs = framerate
    x = wf.readframes(wf.getnframes())
    x = np.frombuffer(x, dtype=np.int16)
    return fs, x


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
    fs, x = read_wave('kyamada/chapter01/sinusoid.wav')
    # save wave file
    save_wave_file('kyamada/chapter01/sinusoid_2', fs, x)
    plt.plot(x)
    plt.show()

    #s_down = s[::2]