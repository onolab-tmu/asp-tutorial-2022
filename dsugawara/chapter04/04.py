import numpy as np
import matplotlib.pyplot as plt


def padding(L, S, x):

    x = np.pad(x, [L - S, L - S])
    temp = S - (x.size % S)  # 末尾に詰める0の個数を求める
    x = np.pad(x, [0, temp])
    return x


def frame_cut(L, S, x):
    N = x.size
    T = ((N - L) // S) + 1  # フレーム数．後で確認
    x_cut = np.empty([T, L])  # 出力
    x_pad = padding(L, S, x)
    for t in range(0, T):
        x_cut[t] = x_pad[t * S : t * S + L]
    return x_cut


def stft(L, S, x):
    x_cut = frame_cut(L, S, x)
    T = x_cut.shape[0]
    win = np.hamming(L)
    X = np.empty((L // 2 + 1, T), dtype="complex")

    for t in range(0, T):
        X[:, t] = np.fft.rfft(win * x_cut[t, :])

    return X


# main
A = 1
f = 440
sf = 16000
sec = 0.1
t = np.arange(0, (sec * sf)) / sf
y = A * np.sin(2 * np.pi * t * f)

L = 1000  # 窓幅
S = 500  # シフト幅

Y = stft(L, S, y)

print(Y)


plt.pcolormesh(np.abs(Y))
plt.savefig("04py_amplitude_spectrogram")

plt.subplot()
plt.pcolormesh(np.angle(Y))
plt.savefig("04py_angle_spectrogram")
