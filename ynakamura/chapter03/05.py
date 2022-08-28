import numpy as np
import matplotlib.pyplot as plt


x = np.zeros((10))
x[0] = 1

y = np.array([])
for n in range(10):
    y = np.append(
        y,
        0.2 * x[n] + 0.2 * x[n - 1] + 0.2 * x[n - 2] + 0.2 * x[n - 3] + 0.2 * x[n - 4],
    )

plt.stem(y)
plt.show()
