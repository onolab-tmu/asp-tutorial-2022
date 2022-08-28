import numpy as np
import matplotlib.pyplot as plt


def frequency_response(a, b, f, fs):
    """
    周波数応答を計算する
    Args:
        a (ndarray): y の係数
        b (ndarray): x の係数
        f (float): 周波数
        fs (float): サンプリング周波数
    Returns:
        H (ndarray): 周波数応答
    """
    omega = 2 + np.pi * f / fs
    sum_a = np.sum(a * np.exp(-1j * omega * np.arange(1, len(a))))
    sum_b = np.sum(b * np.exp(-1j * omega * np.arange(0, len(b))))
    H = sum_b / (1 + sum_a)
    return H


fs = 16000
a = np.array([1, 0.3])
b = np.array([0.4])
N = 10
H = np.zeros(N, dtype="complex")
for i in range(N):
    f = (i / N) * fs
    H[i] = frequency_response(a, b, f, fs)

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.stem(np.abs(H), label="Amplitude")
ax2.stem(np.angle(H), label="Angle")
ax1.grid(True)
ax2.grid(True)
fig.tight_layout()
plt.savefig("outputs/10.pdf")
plt.show()

print("success!")
