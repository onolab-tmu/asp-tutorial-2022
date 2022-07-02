import numpy as np


def linear_convolution(x, h):
    """
    Linear convolution
    Inputs:
        x: input signal
        h: convolution signal
    Returns:
        z: output signal
    """
    N = x.size  # 配列のサイズ
    n = x.size + h.size - 1  # 全体のサイズ
    z = np.zeros(n)  # 出力配列
    for i in range(0, n):
        z[i] = 0
        for k in range(0, N):
            if (i - k) >= 0 and (i - k) < N:  # 入力配列のサイズを超えないようにする
                z[i] += x[k] * h[(i - k)]
    return z


if __name__ == "__main__":
    x = np.array([4, 3, 2, 1])
    h = np.array([1, -1, 1, -1])
    np_convolution = np.convolve(x, h)
    print("Numpy convolution:", np_convolution)
    convolution = linear_convolution(x, h)
    print("My convolution:", convolution)
