import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


def noize_SNR(x, snr):
    sigma = np.sqrt(np.mean(x ** 2) / 10 ** (snr / 10))
    noize = np.random.normal(0, sigma, len(x))
    return noize


if __name__ == "__main__":
    A = 1
    f = 440
    s = 3
    fs = 8000

    t = np.arange(0, s, 1 / fs)
    y, sr = sf.read("sound_re.wav")

    y_avefil = np.convolve(y, np.ones(5), mode="same") / 5

    plt.plot(t, y_avefil)
    plt.xlim([0, 0.03])
    plt.show()
