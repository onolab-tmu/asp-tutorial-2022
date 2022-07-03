import numpy as np


# 関数
def circul_conv_pad(x, h):
    """x[n]とh[n]の巡回たたみこみを計算する（非周期的）

    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）

    Returns:
        y (ndarray): 畳み込み結果（1次元配列）

    """
    x_size = len(x)
    h_size = len(h)

    X = np.fft.fft(np.block([x, np.zeros(h_size)]))
    H = np.fft.fft(np.block([h, np.zeros(x_size)]))
    y = np.fft.ifft(X * H)

    return y[:-1]
