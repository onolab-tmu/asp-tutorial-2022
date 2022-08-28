import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(10)
x[0] = 1

y = np.zeros(10)
y[0] = 0.2 * x[0]
y[1] = 0.2 * x[1] + 0.2 * x[0]
y[2] = 0.2 * x[2] + 0.2 * x[1] + 0.2 * x[0]
y[3] = 0.2 * x[3] + 0.2 * x[2] + 0.2 * x[1] + 0.2 * x[0]
for i in range(4, 10):
    y[i] = (
        0.2 * x[i] + 0.2 * x[i - 1] + 0.2 * x[i - 2] + 0.2 * x[i - 3] + 0.2 * x[i - 4]
    )


plt.stem(y)
plt.savefig("05py_sabun.png")
