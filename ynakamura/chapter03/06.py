import numpy as np
import matplotlib.pyplot as plt


x = np.zeros((10))
x[0] = 1

y = np.zeros((10))
for n in range(10):
    y[n] = 0.3 * y[n - 1] + 0.4 * x[n]


plt.stem(y)
plt.show()
