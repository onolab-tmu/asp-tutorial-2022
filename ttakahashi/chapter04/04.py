import numpy as np
import matplotlib.pyplot as plt


def pad(x, L, S):
    x_pad = np.pad(x, [L - S, L - S])
    re = np.mod(len(x_pad), S)
    if re != 0:
        x_pad = np.pad(x_pad, [0, S - re])
    return x_pad


def frame_div(x, L, S):
    x_pad = pad(x, L, S)
    T = int(np.floor((len(x_pad) - L) / S)) + 1
    x_t = np.zeros((T, L))
    for t in range(T):
        x_t[t] = x_pad[t * S : t * S + L]
    return x_t


def stft(x, L, S, wnd):
    x_t = frame_div(x, L, S)
    T = len(x_t)
    X = np.zeros((T, L // 2 + 1), dtype="complex")
    for t in range(T):
        X[t] = np.fft.rfft(x_t[t] * wnd)
    return X.T


A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 0.1  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成

L = 1000
S = 500
wnd = np.hamming(L)
y_stft = stft(y, L, S, wnd)

fig = plt.figure(figsize=(6, 5))
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2)
ax1.pcolormesh(np.abs(y_stft))
ax2.pcolormesh(np.angle(y_stft))
ax1.set_title("Amplitude spectrum")
ax2.set_title("Phase spectrum")
plt.tight_layout()
plt.savefig("outputs/04.pdf")
plt.show()

print("success!")
