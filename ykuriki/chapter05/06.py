import numpy as np
import matplotlib.pyplot as plt


# 関数
def snr_noise(s, snr):
    """SN比がn[dB]になるようにホワイトノイズを設計する

    Args:
        s (ndarray): 元の信号 (float型1次元配列)
        snr (float): SN比

    Returns:
        eps (ndarray): ノイズ (float型1次元配列)

    """
    np.random.seed(2286)

    alpha = 1 / (10 ** (snr / 20))
    eps = np.random.randn(len(s))
    eps /= np.sqrt(np.sum(eps @ eps))
    eps *= alpha * np.sqrt(np.sum(s @ s))

    return eps


fs = 16000
f = 440
r = 1
sec = 1
snr = 10

t = np.arange(0, fs * sec) / fs
s = r * np.sin(f * 2 * np.pi * t)
eps = snr_noise(s, snr)

x1 = s + eps
x2 = np.block([np.zeros(10), s[:-10]]) + eps
x3 = np.block([np.zeros(20), s[:-20]]) + eps


# プロット
plt.plot(t, x1, label="x1")
plt.plot(t, x2, label="x2")
plt.plot(t, x3, label="x3")
plt.xlabel("time [sec]")
plt.ylabel("amplitude")
plt.xlim([0, 0.01])
plt.grid()
plt.legend()
plt.tight_layout()

plt.show()
