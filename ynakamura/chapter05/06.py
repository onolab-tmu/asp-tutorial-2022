import numpy as np
import matplotlib.pyplot as plt


def adjust_amp(x, snr, fs=16000, sec=3):
    whitenoise = np.random.rand(int(fs * sec)) * 2 - 1
    a = np.sqrt(np.sum(x**2) / np.sum(whitenoise**2) * (10 ** (-snr / 10)))
    whitenoise = a * np.random.rand(int(fs * sec)) - (a / 2)
    return whitenoise


fs = 16000
sec = 1
A = 1
f = 440
t = np.linspace(0, sec, fs * sec)
N = fs * sec

s = A * np.cos(2 * np.pi * f * t)
e = adjust_amp(s, 10, fs, sec)

x_1 = s + e

x_2 = np.zeros((N))
for n in range(N):
    x_2[n] = s[n - 10] + e[n]


x_3 = np.zeros((N))
for n in range(N):
    x_3[n] = s[n - 20] + e[n]

plt.plot(t, x_1, label="x1")
plt.plot(t, x_2, label="x2")
plt.plot(t, x_3, label="x3")
plt.xlim(0, 0.01)
plt.legend()
plt.show()
