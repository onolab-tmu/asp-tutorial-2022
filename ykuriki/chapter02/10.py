import numpy as np
import matplotlib.pyplot as plt


# 関数
def ham_wnd(N):
    """ハミング窓を生成する

    Args:
        N (int): 窓の長さ

    Returns:
        w (ndarray): ハミング窓（float型1次元配列）

    """
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

    return w


def circul_conv(x, h):
    """x[n]とh[n]の巡回たたみこみを計算する

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


fs = 16000
f = 440
r = 1
time = 3

t = np.arange(0, fs * time) / fs
sig = r * np.sin(f * 2 * np.pi * t)
fft_sig = np.fft.fft(sig)

wnd = ham_wnd(len(sig))
fft_wnd = np.fft.fft(wnd)

wnd_sig = np.fft.ifft(circul_conv(fft_sig, fft_wnd))


# プロット
plt.plot(t, wnd_sig)
plt.xlabel("time [sec]")
plt.ylabel("amplitude")
plt.grid()
plt.tight_layout()

plt.show()
