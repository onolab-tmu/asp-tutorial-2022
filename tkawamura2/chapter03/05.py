import numpy as np
import matplotlib.pyplot as plt


def mov_ave(x, M):
    N = x.size
    y = np.zeros(N)
    for n in range(N):
        for i in range(M):
            if n-i >= 0:
                y[n] = y[n] + x[n-i]/M
    return y


x = np.zeros(10)
x[0] = 1

y = mov_ave(x, 5)

plt.stem(y)
plt.show()
