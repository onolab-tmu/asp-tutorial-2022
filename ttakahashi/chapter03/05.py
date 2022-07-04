import numpy as np
import matplotlib.pyplot as plt


def difference_equation(x):
    """
    Args:
        x (ndarray): 入力信号
    Returns:
        x (ndarray): 出力信号
    """
    x[0] = 0.2 * x[0]
    for i in range(1, 4):
        for j in range(i):
            x[i] += 0.2 * x[j]
    for i in range(4, len(x)):
        for j in range(5):
            x[i] += 0.2 * x[i - j]
    return x


x = np.zeros(10)
x[0] = 1
y = difference_equation(x)
plt.stem(y)
plt.grid()
plt.savefig("outputs/05.pdf")
plt.show()

print("success!")
