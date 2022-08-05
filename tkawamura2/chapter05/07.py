from math import ceil
import numpy as np
import matplotlib.pyplot as plt
import librosa


def set_snr(s, snr):
    A_s = np.linalg.norm(s)
    x = np.random.randn(round(len(s)))
    x = A_s * x / (10 ** (snr / 20) * np.linalg.norm(x) ** 2)
    return x


a = 1     # 振幅
fs = 16000  # サンプリング周波数
f = 440  # 周波数
sec = 1   # 秒
snr = 10  # dB

t = np.arange(sec * fs) / fs
y = np.sin(2 * t * np.pi * f)

white_noise = set_snr(y, snr)

x1 = y + white_noise
x2 = np.pad(y[:-9], (9, 0)) + white_noise
x3 = np.pad(y[:-19], (19, 0)) + white_noise
x = np.concatenate([x1.reshape([1, x1.size]), x2.reshape(
    [1, x2.size]), x3.reshape([1, x3.size])], axis=0)

X = librosa.stft(x, n_fft=1024, hop_length=512, window="hann")
F = X.shape[1]
T = X.shape[2]

f = np.arange(ceil(fs / (2 * (F - 1))))
print(f)

w = np.empty([f.size, 3], dtype=np.complex128)
Y = np.empty([f.size, T], dtype=np.complex128)
for j in range(f.size):
    w[j] = np.array([np.exp(-1j * np.pi * j * 0),
                     np.exp(-1j * np.pi * j * 10 / fs),
                     np.exp(-1j * np.pi * j * 20 / fs)]) / 3
    Y[j] = np.dot(np.conj(w[j]), X[:, j, :])

enhanced = librosa.istft(Y, hop_length=512, n_fft=1024, window="hann")

plt.plot(enhanced)
plt.xlim(0, 0.01 * fs)
plt.show()
