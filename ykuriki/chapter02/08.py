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


fs = 16000
f = 440
r = 1
sec = 3

t = np.arange(0, fs * sec) / fs
sig = r * np.sin(f * 2 * np.pi * t)

wnd = ham_wnd(len(sig))

wnd_sig = sig * wnd


# プロット
plt.plot(t, wnd_sig)
plt.xlabel("time [sec]")
plt.ylabel("amplitude")
plt.grid()
plt.tight_layout()

plt.show()
