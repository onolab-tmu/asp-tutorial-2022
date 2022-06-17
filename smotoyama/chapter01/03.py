import numpy as np
import soundfile as sf


def create_sound(A, f, t):
    x = A * np.sin(2 * np.pi * f * t)
    return x


if __name__ == "__main__":
    A = 1
    f_1 = 440
    f_2 = 660
    fs = 16000
    s = 3

    t = np.arange(0, s, 1 / fs)
    x_1 = A * np.sin(2 * np.pi * f_1 * t)
    x_2 = A * np.sin(2 * np.pi * f_2 * t)

    x = np.array([x_1, x_2])

    sf.write("sound_2ch.wav", data=x.T, samplerate=fs, subtype="PCM_16")
