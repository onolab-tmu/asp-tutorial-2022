import numpy as np


def cul_SNR(y, x):
    snr = 10 * np.log10(np.sum(y ** 2) / np.sum(x ** 2))
    return snr
