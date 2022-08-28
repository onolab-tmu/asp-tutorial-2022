import numpy as np
import matplotlib.pyplot as plt


# 関数
def clc_freq_resp(a, b, f, fs):
    """周波数応答を計算する

    Args:
        a (ndarray): yの係数（1次元配列）
        b (ndarray): xの係数（1次元配列）
        f (double): 周波数
        fs (double): サンプリング周波数


    Returns:
        H (complex): 周波数応答

    """
    N = len(a)
    M = len(b)
    omega = 2 * np.pi * f / fs

    H = np.sum(b * np.exp(-1j * omega * np.arange(M))) / (
        1 + np.sum(a[1:] * np.exp(-1j * omega * np.arange(1, N)))
    )

    return H


fs = 16000
N = 32
f = np.arange(N) / N * fs
a = np.array([1])
b = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
H = np.zeros(N, dtype="complex")

for i in range(N):
    H[i] = clc_freq_resp(a, b, f[i], fs)

amp = np.abs(H)
phase = np.angle(H)


# プロット
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 5))

p0 = ax[0].stem(f, amp)
ax[0].set_xlabel("f")
ax[0].set_ylabel("amplitude")
ax[0].set_title("Amplitude")
ax[0].grid()

p0 = ax[1].stem(f, phase)
ax[1].set_xlabel("f")
ax[1].set_ylabel("phase")
ax[1].set_title("Phase")
ax[1].grid()

plt.tight_layout()

plt.show()
