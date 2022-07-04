import numpy as np
import matplotlib.pyplot as plt


length = 10
x = np.array([1])
a = 0.3
b = 0.4
y = np.zeros(length)

# n = 0
y[0] += b * x[0]

# n > 0
for n in range(1, length):
    y[n] += a * y[n - 1]


# プロット
plt.stem(np.arange(length), y)
plt.xlabel("n")
plt.ylabel("amplitude")
plt.grid()
plt.tight_layout()

plt.show()
