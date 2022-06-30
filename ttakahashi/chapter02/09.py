import numpy as np


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

N = sec * sr
w = hamming(N)
w_fft = np.fft.fft(w)

print("success!")
