import numpy as np
import better_exceptions
better_exceptions.MAX_LENGTH = None


def generate_snr_noise(snr, s1, t2, s2):    # 指定したSN比になるように信号の振幅を調整
    s2 = s2 / np.sqrt(np.sum(s2 ** 2))
    s2 = s2 * np.sqrt(np.sum(s1 ** 2))
    s2 = s2 * 10 ** (-1 * snr / 20)
    return t2, s2
