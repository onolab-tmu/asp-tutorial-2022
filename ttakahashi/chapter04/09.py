import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sp


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


sec = 1  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = sp.chirp(t, 100, sec, 16000)
L = np.array([100, 200, 400, 800])

fig, ax = plt.subplots(2, 2, figsize=(7, 7))

for i in range(len(L)):
    S = int(L[i] / 2)
    wnd = np.hamming(L[i])
    C = stft(y, L[i], S, wnd)
    ax[i // 2, i % 2].pcolormesh(20 * np.log10(np.abs(C)))
    ax[i // 2, i % 2].set_title(str(L[i]) + "/" + str(S))

plt.tight_layout()
plt.savefig("outputs/09.pdf")
plt.show()

print("success!")
