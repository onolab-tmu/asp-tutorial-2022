import numpy as np
import matplotlib.pyplot as plt


def adjust_amp(x, snr, fs=16000, sec=3):
    whitenoise = np.random.rand(int(fs * sec)) * 2 - 1
    a = np.sqrt(np.sum(x**2) / np.sum(whitenoise**2) * (10 ** (-snr / 10)))
    whitenoise = a * np.random.rand(int(fs * sec)) * 2 - 1
    return whitenoise


fs = 16000
sec = 3
fin = 440
t = np.linspace(0.0, sec, int(fs * sec))

x = np.sin(2.0 * np.pi * fin * t)

whitenoise = adjust_amp(x, 6)
mix = x + whitenoise

mix_filtered = np.array([])
for i in range(mix.shape[0] - 4):
    tmp = 0
    for j in range(5):
        tmp += mix[i + j]
    mix_filtered = np.append(mix_filtered, tmp / 5)

plt.plot(t[: mix_filtered.shape[0]], mix[: mix_filtered.shape[0]], label="original")
# plt.plot(t, mix_filtered, label="original")
plt.plot(t[: mix_filtered.shape[0]], mix_filtered, label="filtered")
plt.xlim(0, 0.03)
plt.legend()
plt.show()
