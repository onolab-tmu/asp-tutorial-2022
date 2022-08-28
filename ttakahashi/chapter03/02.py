import numpy as np


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


impulse = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
kernel = [4, 3, 2, 1, 0, 0]
print(circle_conv(impulse, kernel))
print(np.convolve(impulse, kernel))

print("success!")
