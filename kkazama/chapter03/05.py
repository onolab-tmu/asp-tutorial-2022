from wsgiref.headers import tspecials
import numpy as np
from matplotlib import pyplot as plt


def f(x):
    y = np.zeros(len(x))
    for n in range(len(x)):
        for k in range(5):
            m = n - k
            if m >= 0:
                y[n] += 0.2 * x[m]

    return y


x = np.zeros(10)
x[0] = 1
y = f(x)

plt.stem(y)

plt.show()
