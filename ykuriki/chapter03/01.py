import numpy as np


# 関数
def line_conv(x, h):
    """線形たたみこみを行う

    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）

    Returns:
        y (ndarray): 畳み込みの実行結果（1次元配列）

    """
    x_size = len(x)
    h_size = len(h)
    y_size = x_size + h_size - 1

    y = np.zeros(y_size)

    # 纏めて計算
    for i in range(x_size):
        y[i : i + h_size] += x[i] * h

    return y
