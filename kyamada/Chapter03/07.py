import numpy as np
import matplotlib.pyplot as plt


def difference_equation(x, a, b):
    """
    差分方程式
    Input
        x : input signal
        a : coefficient of y
        b : coefficient of x
    Output
        y: output signal
    """

    N = a.size
    M = b.size
    L = x.size
    y = np.zeros(L)

    for n in range(0, L):
        # a についての処理
        for k in range(1, N):
            y[n] -= a[k] * y[n - k]
        # b についての処理
        for k in range(0, M):
            if (n - k) >= 0 or (n - k) < N or n > N:  # 入力配列のサイズを超えないようにする
                y[n] += b[k] * x[n - k]

    y = y / a[0]
    return y


if __name__ == "__main__":
    x = np.zeros(10)
    x[0] = 1
    a = np.array([1, -0.3])
    b = np.array([0.4])
    y = difference_equation(x, a, b)

    plt.stem(y)
    plt.grid()
    plt.show()
