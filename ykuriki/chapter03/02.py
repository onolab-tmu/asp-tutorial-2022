import numpy as np


# 関数
def circul_conv(x, h):
    """x[n]とh[n]の巡回たたみこみを計算する（周期的）

    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）

    Returns:
        y (ndarray): 畳み込み結果（1次元配列）

    """
    X = np.fft.fft(x)
    H = np.fft.fft(h)
    y = np.fft.ifft(X * H)

    return y
