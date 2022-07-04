import numpy as np
import matplotlib.pyplot as plt


def difference_equation(x, a, b):
    """
    一般化差分方程式
    Args:
        x (ndarray): 入力信号
        a (ndarray): y の係数
        b (ndarray): x の係数
    Returns:
        y (ndarray): 出力信号
    """
    y = np.zeros(len(x))
    for n in range(0, len(x)):
        for k in range(1, len(a)):
            y[n] -= a[k] * y[n - k]
        for k in range(0, len(b)):
            if (n - k) >= 0 or (n - k) < len(a) or n > len(a):  # 入力配列のサイズを超えないようにする
                y[n] += b[k] * x[n - k]
    y = y / a[0]
    return y


x = np.zeros(10)
x[0] = 1
a = np.array([1, -0.3])
b = np.array([0.4])
y = difference_equation(x, a, b)
plt.stem(y)
plt.grid()
plt.savefig("outputs/07.pdf")
plt.show()

print("success!")
