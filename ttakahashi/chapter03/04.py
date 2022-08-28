import numpy as np
import matplotlib.pyplot as plt


def linear_conv(x, h):
    """
    x[n]とh[n]の線形畳み込みを計算する
    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）
    Returns:
        y (ndarray): 畳み込み結果（1次元配列）
    """
    y = np.zeros(len(h) + len(x) - 1, dtype=np.float32)
    for k in range(0, len(y)):
        y[k] = 0.0
        for m in range(0, len(x)):
            n = k - m
            if n >= 0 and n < len(h):
                y[k] += x[m] * h[n]
    return y


def circle_conv(x, h):
    """
    x[n]とh[n]の巡回畳み込みを計算する
    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）
    Returns:
        y (ndarray): 畳み込み結果（1次元配列）
    """
    y = np.zeros(len(h) + len(x) - 1, dtype=np.float32)
    for k in range(0, len(y)):
        y[k] = 0.0
        for m in range(0, len(x)):
            n = k - m
            if n >= 0 and n < len(h):
                index = (k - m) % len(x)
                y[k] += x[m] * h[index]
    return y


def circle_conv_pad(x, h):
    """
    x[n]とh[n]の巡回畳み込みを零詰めを行って計算する
    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）
    Returns:
        y (ndarray): 畳み込み結果（1次元配列）
    """
    y = np.zeros(len(h) + len(x) - 1, dtype=np.float32)
    x = np.pad(x, (0, len(x) - 1), "constant")
    h = np.pad(h, (0, len(x) - 1), "constant")
    for k in range(0, len(y)):
        y[k] = 0.0
        for m in range(0, len(x)):
            n = k - m
            if n >= 0 and n < len(h):
                index = (k - m) % len(x)
                y[k] += x[m] * h[index]
    return y


impulse = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
kernel = [4, 3, 2, 1, 0, 0]
linear = linear_conv(impulse, kernel)
circle = circle_conv(impulse, kernel)
circle_pad = circle_conv_pad(impulse, kernel)
fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)
ax1.stem(linear, label="linear")
ax2.stem(circle, label="circle")
ax3.stem(circle_pad, label="circle_pad")
ax1.grid(True)
ax2.grid(True)
ax3.grid(True)
fig.tight_layout()
plt.savefig("outputs/04.pdf")
plt.show()

print("success!")
