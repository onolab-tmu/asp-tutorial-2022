import numpy as np


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

    return X
