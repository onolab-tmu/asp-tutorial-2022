import numpy as np
import matplotlib.pyplot as plt


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


def circular_convolution(x, y):
    N = max(len(x), len(y))
    n = np.arange(N)
    z = np.zeros(N, dtype="complex")

    for k in range(N):
        z[k] = np.sum(x[n] * y[(k - n) % N])
    return z / N


if __name__ == "__main__":
    a = 1.0  # 振幅
    sec = 3  # 信号長
    sr = 16000  # サンプリング周波数
    f = 440  # 周波数

    t = np.arange(0, sec * sr) / sr
    signal = a * np.sin(2 * np.pi * f * t)
    window = hamming(len(signal))
    x = np.fft.fft(signal)
    y = np.fft.fft(window)
    z = circular_convolution(x, y)
    idft_z = np.fft.ifft(z)
    window_signal = window * signal

    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].plot(idft_z.real)
    ax[1].plot(window_signal)
    plt.tight_layout()
    plt.show()
