import numpy as np
import matplotlib.pyplot as plt


def difference_equation(x):
    """
    Args:
        x (ndarray): 入力信号
    Returns:
        y (ndarray): 出力信号
    """
    y = np.zeros(len(x))
    y[0] = 0.4 * x[0]
    for i in range(1, len(x)):
        y[i] = 0.3 * y[i - 1] + 0.4 * x[i]
    return y


x = np.zeros(10)
x[0] = 1
y = difference_equation(x)
plt.stem(y)
plt.grid()
plt.savefig("outputs/06.pdf")
plt.show()

print("success!")
