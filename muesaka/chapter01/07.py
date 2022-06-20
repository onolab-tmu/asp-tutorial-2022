import numpy as np
import better_exceptions
better_exceptions.MAX_LENGTH = None


def calculate_snr(s1, s2):  # SN比計算
    s1 = np.sum(np.array(s1) ** 2)
    s2 = np.sum(np.array(s2) ** 2)
    snr = 10 * np.log10(s1/s2, 10)
    return snr
