from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt

# 線形畳み込み
def conv(x, h):
    N = len(x)
    y = np.zeros(len(x) + len(h) - 1)

    for n in range(len(y)):  # n = 0,..., 2N-2
        y[n] = 0  # 初期化
        for k in range(len(x)):
            m = n - k
            if (m >= 0) and (m <= N - 1):
                y[n] += x[k] * h[m]

    return y


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


# ゼロ詰め巡回畳み込み
def pad_circular_conv(x, h):
    N = len(x)  # 信号の長さ
    y = np.zeros(len(x) + len(h) - 1)

    x = np.pad(x, (0, len(h) - 1))
    h = np.pad(h, (0, len(x) - 1))

    for n in range(len(y)):
        y[n] = 0  # 初期化
        for k in range(len(x)):
            m = n - k
            if (m >= 0) and (m <= N - 1):
                y[n] += x[k] * h[m % N]

    return y


x = np.arange(4, 1, -1)
y = [1, 0, -1, 0]

z1 = conv(x, y)
z2 = circular_conv(x, y)
z3 = pad_circular_conv(x, y)

plt.subplot(3, 1, 1)
plt.stem(z1)

plt.subplot(3, 1, 2)
plt.stem(z2)

plt.subplot(3, 1, 3)
plt.stem(z3)

plt.show()
