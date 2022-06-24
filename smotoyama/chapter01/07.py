import numpy as np


def adj_SNR(x, snr):
    n = np.random.rand(round(len(x)))
    sigma = np.sqrt(np.sum(x ** 2) / np.sum(n ** 2) * 10 ** (-snr / 10))
    noize = sigma * n
    y = x + noize
    return y
