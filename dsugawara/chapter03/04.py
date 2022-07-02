import numpy as np
import matplotlib.pyplot as plt


# 線形畳み込み
def Liner_convolution(x, h):
    N = x.size
    z = np.zeros(2 * (N - 1))

    for n in range(2 * (N - 1)):
        for k in range(N):
            if 0 <= n - k and n - k <= N - 1:
                z[n] += x[k] * h[n - k]

    return z


# 巡回畳み込み
def Circlar_convolution(x, h):

    N = x.size
    z = np.zeros(N)

    for n in range(0, N):
        for k in range(0, N):
            z[n] += x[k] * h[(n - k) % N]

    return z


# ゼロ詰めした巡回畳み込み
def Circar_convolution_padded(x, h):

    x = np.pad(x, [0, h.size - 1])
    h = np.pad(h, [0, x.size - 1])
    N = x.size
    z = np.zeros(N)

    for n in range(0, N):
        for k in range(0, N):
            z[n] += x[k] * h[(n - k) % N]

    return z


# main
x = np.array([4, 3, 2, 1])
h = np.array([1, 0, -1, 0])

liner_conv = Liner_convolution(x, h)
circle_conv = Circlar_convolution(x, h)
circle_conv_padded = Circar_convolution_padded(x, h)


# plot
fig = plt.figure()
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)
ax1.stem(liner_conv)
ax2.stem(circle_conv)
ax3.stem(circle_conv_padded)
ax1.set_title("liner convolution")
ax2.set_title("circular convolution")
ax3.set_title("circular convolution (padded)")
fig.tight_layout()
plt.savefig("04py_compare.png")
