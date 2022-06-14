import numpy as np
import matplotlib.pyplot as plt


def adjust_amp(x, snr, fs=16000, sec=3):
    whitenoise = np.random.rand(int(fs * sec)) * 2 - 1
    a = np.sqrt(np.sum(x ** 2) / np.sum(whitenoise ** 2) * (10 ** (-snr / 10)))
    print(np.sum(whitenoise ** 2))
    whitenoise = a * np.random.rand(int(fs * sec)) * 2 - 1
    return whitenoise