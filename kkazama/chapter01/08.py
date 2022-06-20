import numpy as np

#SNR計算
def cal_sn(s, x):
    snr = 10 * np.log10(np.sum(s * s) / np.sum(x * x))

    return snr

#ノイズの振幅調整
def cal_adj_amp(s, x, snr):
    x = x / np.sqrt(sum(x * x))
    x = x * np.sqrt(sum(s * s))
    x = x * 10 ** (-snr / 20)

    return x