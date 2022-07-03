import numpy as np
import matplotlib.pyplot as plt


def hamming(N):
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))
    return w


def circul_conv(x, h):
    """
    x[n]とh[n]の巡回畳み込みを計算する
    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）
    Returns:
        y (ndarray): 畳み込み結果（1次元配列）
    """
    x_size = len(x)
    h_size = len(h)
    fft_size = max(x_size, h_size)
    X = np.fft.fft(np.block([x, np.zeros(fft_size - h_size)]))
    H = np.fft.fft(np.block([h, np.zeros(fft_size - x_size)]))
    y = np.fft.ifft(X * H) / fft_size
    return y


A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成
y_fft = np.fft.fft(y)

N = sec * sr
w = hamming(N)
w_fft = np.fft.fft(w)

y_wnd = np.fft.ifft(circul_conv(y_fft, w_fft))

plt.plot(y_wnd)
plt.xlabel("time [sec]")
plt.ylabel("amplitude")
plt.grid()
plt.savefig("outputs/10.pdf")
plt.show()

print("success!")
