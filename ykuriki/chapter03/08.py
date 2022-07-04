import numpy as np


# 関数
def clc_freq_resp(a, b, f, fs):
    """周波数応答を計算する

    Args:
        a (ndarray): yの係数（1次元配列）
        b (ndarray): xの係数（1次元配列）
        f (double): 周波数
        fs (double): サンプリング周波数


    Returns:
        H (complex): 周波数応答

    """
    N = len(a)
    M = len(b)
    omega = 2 * np.pi * f / fs

    H = np.sum(b * np.exp(-1j * omega * np.arange(M))) / (
        1 + np.sum(a[1:] * np.exp(-1j * omega * np.arange(1, N)))
    )

    return H
