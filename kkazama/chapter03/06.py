from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt


def f(x):
    y = np.zeros(len(x))
    for k in range(len(x)):
        if k == 0:
            y[k] = 0.4 * x[k]
        else:
            y[k] = 0.3 * y[k - 1] + 0.4 * x[k]
    return y


x = np.zeros(10)
x[0] = 1
y = f(x)

plt.stem(y)

plt.show()
