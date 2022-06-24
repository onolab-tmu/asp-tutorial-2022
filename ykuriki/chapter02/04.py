import numpy as np
import matplotlib.pyplot as plt


# 関数
def clc_dft(x):
    """x[n]の離散フーリエ変換(DFT)を計算する

    Args:
        x (ndarray): 信号 (float型1次元配列)

    Returns:
        X (ndarray): 信号のDFT (complex型1次元配列)

    """
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N, dtype="complex64")

    for k in range(N):
        X[k] = np.sum(x[n] * np.exp(-2j * np.pi * k * n / N))

    return X


delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])

dft_delta = clc_dft(delta)

amp = np.abs(dft_delta)
phase = np.angle(dft_delta)

k = np.arange(len(dft_delta))


# プロット
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 5))

p0 = ax[0].stem(k, amp)
ax[0].set_xlabel("k")
ax[0].set_ylabel("amplitude spectrum")
ax[0].set_title("Amplitude spectrum")
ax[0].grid()

p0 = ax[1].stem(k, phase)
ax[1].set_xlabel("k")
ax[1].set_ylabel("phase spectrum")
ax[1].set_title("Phase spectrum")
ax[1].grid()

plt.tight_layout()

plt.show()
