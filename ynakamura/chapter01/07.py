import numpy as np
import matplotlib.pyplot as plt


def calculate_snr(signal, noise):
    return 10 * np.log(np.sum(signal ** 2) / np.sum(noise ** 2))