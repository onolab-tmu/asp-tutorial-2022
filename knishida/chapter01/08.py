import numpy as np


def SNratio(s, x):
    ssum = 0.0
    xsum = 0.0
    for i in range(len(s)):
        ssum += s[i] ** 2
        xsum += x[i] ** 2
    return 10 * np.log10(ssum / xsum)


def ajust_SN(s, x, SN):
    ssum = 0.0
    xsum = 0.0
    for i in range(len(s)):
        ssum += s[i] ** 2
        xsum += x[i] ** 2
    return np.sqrt(ssum / xsum * 10 ** (-SN / 10))


if __name__ == "__main__":
    A = 1
    f = 440.0
    sec = 3.0
    fs = 16000
    SN = 12

    t = np.arange(0, sec, 1 / fs)
    y = A * np.sin(2 * np.pi * f * t)
    n = np.random.rand(round(fs * sec))

    X = ajust_SN(y, n, SN)

    print(SNratio(y, X * n))
