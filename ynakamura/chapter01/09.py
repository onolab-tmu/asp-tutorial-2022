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

whitenoise = adjust_amp(x, 20)
mix = x + whitenoise

plt.plot(t, mix)
plt.xlim(0, 0.03)
plt.show()


# SNR確認用コード
def calculate_snr(signal, noise):
    return 10 * np.log(np.sum(signal**2) / np.sum(noise**2))


print(calculate_snr(x, whitenoise))
