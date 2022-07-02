from turtle import color
import numpy as np
import matplotlib.pyplot as plt


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


def circle_convolution(x, h):
    """
    Circle convolution
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
            index = (i - k) % N
            print(x[k], h[index])
            z[i] += x[k] * h[index]
    return z


def circle2_convolution(x, h):
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
            z[i] += x[k] * h[index]
    return z[:n_size]


if __name__ == "__main__":
    x = np.array([4, 3, 2, 1])
    h = np.array([1, -1, 1, -1])
    np_convolution = np.convolve(x, h)
    #print("Numpy convolution:", np_convolution)
    linear_convolution = linear_convolution(x, h)
    print("linear convolution:", linear_convolution)
    circle_convolution = circle_convolution(x, h)
    print("circle convolution:", circle_convolution)
    circle2_convolution = circle2_convolution(x, h)
    print("circle2 convolution:", circle2_convolution)

    plt.subplot(3, 1, 1)
    plt.stem(linear_convolution, label="linear")
    plt.subplot(3, 1, 2)
    plt.stem(circle_convolution, label="circle")
    plt.subplot(3, 1, 3)
    plt.stem(circle2_convolution, label="circle2")
    # plt.grid()
    plt.tight_layout()
    plt.show()
