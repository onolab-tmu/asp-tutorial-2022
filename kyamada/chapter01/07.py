import numpy as np


def calcrate_snr(x, s):
    """
    Calculate SNR
    Input:
        x: wave data
        s: noise data
    Output:
        snr: SNR
    """
    snr = 10 * np.log10(np.sum(x ** 2)/np.sum(s ** 2))
    return snr


if __name__ == '__main__':
    x = 100 * np.sin(2 * np.pi * 400)
    s = 1 * np.sin(2 * np.pi * 880)
    snr = calcrate_snr(x, s)
    print(snr)
