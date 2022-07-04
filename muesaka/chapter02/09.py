import numpy as np


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


if __name__ == "__main__":
    a = 1.0  # 振幅
    sec = 3  # 信号長
    sr = 16000  # サンプリング周波数
    f = 440  # 周波数

    t = np.arange(0, sec * sr) / sr
    signal = a * np.sin(2 * np.pi * f * t)
    window = hamming(len(signal))
    dft_window = np.fft.fft(window)

    print(dft_window)
