import numpy as np
import matplotlib.pyplot as plt


length = 10
x = np.array([1])
b = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
y = np.zeros(length)

for n in range(length):
    for k in range(len(b)):
        if k <= n and n - k < len(x):
            y[n] += b[k] * x[n - k]


# プロット
plt.stem(np.arange(length), y)
plt.xlabel("n")
plt.ylabel("amplitude")
plt.grid()
plt.tight_layout()

plt.show()
