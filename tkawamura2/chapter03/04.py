import numpy as np
import matplotlib.pyplot as plt


def liner_conv(x, h):
    N = x.size
    M = x.size + h.size - 1
    z = np.zeros(M)
    for n in range(M):
        for k in range(N):
            if n-k >= 0 and n-k <= N - 1:
                z[n] = z[n] + x[k]*h[n-k]
    return z


def circ_conv(x, h):
    N = x.size
    M = h.size
    z = np.zeros(M)
    for n in range(M):
        for k in range(N):
            z[n] = z[n] + x[k]*h[np.mod(n-k, M)]
    return z


def circpad_linerconv(x, h):
    N = x.size
    h = np.pad(h, [0, int(N / 2) + 1])
    M = h.size
    z = np.zeros(M)
    for n in range(M):
        for k in range(N):
            z[n] = z[n] + x[k]*h[np.mod(n-k, M)]
    return z


x = np.array([4, 3, 2, 1])
y = np.array([1, 0, -1, 0])

liconv = liner_conv(x, y)
ciconv = circ_conv(x, y)
ciliconv = circpad_linerconv(x, y)

plt.stem(liconv)
plt.show()

plt.stem(ciconv)
plt.show()

plt.stem(ciliconv)
plt.show()
