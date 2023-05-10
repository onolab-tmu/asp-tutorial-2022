import numpy as np
import scipy.signal as sp
import matplotlib.pyplot as plt


def padding(L, S, x):

    x = np.pad(x, [L - S, L - S])
    temp = S - (x.size % S)  # 末尾に詰める0の個数を求める
    x = np.pad(x, [0, temp])
    return x


def frame_cut(L, S, x):
    N = x.size
    T = ((N - L) // S) + 1  # フレーム数．後で確認
    x_cut = np.zeros((T, L))  # 出力
    x_pad = padding(L, S, x)
    for t in range(0, T):
        xt = np.zeros(L)
        for l in range(0, L):
            xt[l] = x_pad[t * S + l]
        x_cut[t] = xt

    return x_cut


def stft(L, S, x):
    x_cut = frame_cut(L, S, x)
    T = x_cut.shape[0]  # フレーム数
    win = np.hamming(L)
    X = np.empty((L // 2 + 1, T), dtype="complex")

    for t in range(0, T):
        X[:, t] = np.fft.rfft(win * x_cut[t, :])

    return X


# main
sf = 16000
sec = 1
t = np.arange(0, sec * sf) / sf

chirp = sp.chirp(t, 100, sec, 16000)

window_width = [100, 200, 400, 800]  # 窓長の変移

for L in window_width:
    Y = stft(L, L // 2, chirp)
    plt.subplot()
    plt.pcolormesh(np.abs(Y))
    plt.savefig("09py_" + str(L) + ".png")
