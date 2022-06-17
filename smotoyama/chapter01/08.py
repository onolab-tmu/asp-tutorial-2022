import numpy as np
import soundfile as sf


def cul_SNR(y, x):
    snr = 10 * np.log10(np.sum(y ** 2) / np.sum(x ** 2))
    return snr


def adj_SNR(x, snr):
    n = np.random.rand(round(len(x)))
    sigma = np.sqrt(np.sum(x ** 2) / np.sum(n ** 2) * 10 ** (-snr / 10))
    noize = sigma * n
    y = x + noize
    return y


if __name__ == "__main__":
    A = 1
    f = 440
    s = 3
    fs = 16000
    SN = 6

    t = np.arange(0, s, 1 / fs)
    x = A * np.sin(2 * np.pi * f * t)

    y = adj_SNR(x, SN)

    sf.write("sound_noize.wav", data=y, samplerate=fs, subtype="PCM_16")
