from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

# 線形畳み込み
def conv(x, h):
    N = len(x)
    y = np.zeros(len(x) + len(h) - 1)
    for n in range(len(y)): # n = 0,..., 2N-2
        y[n] = 0 #初期化
        for k in range(len(x)):
            m = n - k
            if (n - k >= 0) and (n - k <= N - 1):
                y[n] += x[k] * h[m]
    
    return y

