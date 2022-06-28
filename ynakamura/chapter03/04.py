import numpy as np
import matplotlib.pyplot as plt


def linear_conv(x, h):
    N = x.shape[0]
    z = np.array([])
    for n in range(2 * N - 1):
        sum = 0
        for k in range(N):
            if n - k >= 0 and n - k <= N - 1:
                sum += x[k] * h[n - k]
            else:
                sum += 0
        z = np.append(z, sum)
    return z


def circular_conv(x, h):
    N = x.shape[0]
    z = np.array([])
    for n in range(N - 1):
        sum = 0
        for k in range(N):
            sum += x[k] * h[(n - k) % N]
        z = np.append(z, sum)
    return z


def zeropad_circular_conv(x, h):
    x = np.pad(x, (0, x.shape[0] - 1))
    h = np.pad(h, (0, h.shape[0] - 1))
    N = x.shape[0]
    z = np.array([])
    for n in range(N):
        sum = 0
        for k in range(N - 1):
            sum += x[k] * h[(n - k) % N]
        z = np.append(z, sum)
    return z


x = np.array([4, 3, 2, 1])
y = np.array([1, 0, -1, 0])

linear = linear_conv(x, y)
circular = circular_conv(x, y)
zeropad_circular = zeropad_circular_conv(x, y)

plt.stem(linear)
plt.title("linear_conv")
plt.show()

plt.stem(circular)
plt.title("circular_conv")
plt.show()

plt.stem(zeropad_circular)
plt.title("zeropad_circular_conv")
plt.show()
