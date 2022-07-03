import numpy as np


def circle_convolution(x, h):
    """
    Circle convolution with padding

    Inputs:
        x: input signal
        h: convolution signal
    Returns:
        z: output signal
    """
    N = x.size  # 配列のサイズ
    n_size = x.size + h.size - 1  # 全体のサイズ
    x = np.pad(x, (0, N-1), 'constant')  # zero-padding
    h = np.pad(h, (0, N-1), 'constant')  # zero-padding
    N = x.size
    n = x.size + h.size - 1  # 全体のサイズ
    z = np.zeros(n)  # 出力配列
    for i in range(0, n):
        z[i] = 0
        for k in range(0, N):
            index = (i - k) % N
            print(x[k], h[index])
            z[i] += x[k] * h[index]
    return z[:n_size]


if __name__ == "__main__":
    x = np.array([4, 3, 2, 1])
    h = np.array([1, -1, 1, -1])
    np_convolution = np.convolve(x, h)
    print("Numpy convolution:", np_convolution)
    convolution = circle_convolution(x, h)
    print("My convolution:", convolution)
