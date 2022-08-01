import numpy as np
import matplotlib.pyplot as plt


def make_noise(signal, is_SNR):

    """SNRを調整した雑音を生成する

    Args:
        signal (ndarray): 信号（1次元配列）
        is_SNR (double): SNR

    Return:
        ndarray: 雑音

    """
    noise = np.random.randn(len(signal))

    noise = noise / np.sqrt(np.sum(noise**2))
    noise = noise * np.sqrt(np.sum(signal**2))
    noise = noise * 10 ** (-1 * is_SNR / 20)

    return noise


# main
A = 1.0
fs = 16000
sec = 1
f = 440
t = np.arange(0, fs * sec) / fs

s = A * np.sin(2 * np.pi * f * t)

noise = make_noise(s, 10)

x1 = s + noise
s2 = np.pad(s, [10, 0])
x2 = s2[0 : len(s2) - 10] + noise
s3 = np.pad(s, [20, 0])
x3 = s3[0 : len(s3) - 20] + noise

# plot
plt.xlim(0, fs * 0.01)
plt.plot(x1)
plt.plot(x2)
plt.plot(x3)
plt.savefig("06py_signal.png")
