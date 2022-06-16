# 信号長の等しい 2 個の信号 の信号対雑音比(SN比) を計算する関数を実装せよ．

import numpy as np


def culclation_SNR(s, x, n):
    i = 0
    s2 = 0      # s[n]の2乗
    x2 = 0      # x[n]の2乗

    while i < n:
        s2 = s2 + s[n]**2
        x2 = x2 + x[n]**2
        i+=1

    SNR = 10 * np.log10(s2/x2)

    return SNR