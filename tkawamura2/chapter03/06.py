import numpy as np
import matplotlib.pyplot as plt


x = np.zeros(10)
x[0] = 1

N = x.size
y = np.zeros(N)
y[0] = 0.4*x[0]

for n in np.arange(1, N):
    y[n] = 0.3*y[n-1] + 0.4*x[n]

plt.stem(y)
plt.show()
