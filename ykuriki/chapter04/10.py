import numpy as np
import matplotlib.pyplot as plt


# 関数
def zero_pad(x, L, S):
    """x[n]に零詰めする

    Args:
        x (ndarray): 信号（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: 零詰めされた信号

    """
    x = np.block([np.zeros(L - S), x, np.zeros(L - S)])

    if len(x) % S != 0:
        x = np.block([x, np.zeros(S - (len(x) % S))])

    return x


def frame_div(x, L, S):
    """x[n]をフレーム分割する

    Args:
        x (ndarray): 信号（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: フレーム分割された信号

    """
    x = zero_pad(x, L, S)
    T = int(np.floor((len(x) - L) / S)) + 1
    xt = np.zeros((T, L))

    for t in range(T):
        xt[t] = x[t * S : t * S + L]

    return xt


def clc_stft(x, w, L, S):
    """x[n]のSTFTを計算する

    Args:
        x (ndarray): 信号（1次元配列）
        w (ndarray): 窓関数（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: x[n]のSTFT

    """
    x = frame_div(x, L, S)
    T = len(x)
    X = np.zeros((T, L // 2 + 1), dtype="complex")

    for t in range(T):
        X[t] = np.fft.rfft(x[t] * w)

    return X.T


def clc_axis(X, fs, S):
    """縦軸を周波数，横軸を時間に変換する

    Args:
        X (ndarray): スペクトログラム
        fs (int): サンプリング周波数
        S (int): シフト幅

    Returns:
        freq (ndarray): 縦軸（周波数）
        time (ndarray): 横軸（時間）

    """
    F = len(X)
    T = len(X[0])
    L = (F - 1) * 2
    freq = np.arange(F + 1) / F * fs / 2
    time = (np.arange(T + 1) * S - (L - S)) / fs

    return freq, time


fs = 16000
f = 440
r = 1
sec = 0.1
L = 1000
S = 500

t = np.arange(fs * sec) / fs
x = r * np.sin(f * 2 * np.pi * t)
w = np.hamming(L)

X = clc_stft(x, w, L, S)

freq, time = clc_axis(X, fs, S)


# プロット
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 5))

p0 = ax[0].pcolormesh(time, freq, np.abs(X))
ax[0].set_xticks(time)
ax[0].set_title("Amplitude spectrum")

p1 = ax[1].pcolormesh(time, freq, np.angle(X))
ax[1].set_xticks(time)
ax[1].set_title("Phase spectrum")

plt.tight_layout()

plt.show()
