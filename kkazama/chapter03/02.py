from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

# 巡回畳み込み
def circular_conv(x, h):
    N = len(x)  # 信号の長さ
    y = np.zeros(N)

    for n in range(len(y)):
        y[n] = 0  # 初期化
        for k in range(len(x)):
            m = n - k
            if (m >= 0) and (m <= N - 1):
                y[n] += x[k] * h[m % N]

    return y

