import numpy as np


def frequency_response(a, b, f, fs):
    """
    周波数応答を計算する
    Input:
         a : coefficient of y
        b : coefficient of x
        f: 周波数
        fs: サンプリング周波数
    Output:
        H: 周波数応答
    """
    N = a.size
    M = b.size

    omega = 2 + np.pi * f / fs
    # a についての処理
    sum_a = np.sum(a * np.exp(-1j * omega * np.arange(1, N)))
    # b についての処理
    sum_b = np.sum(b * np.exp(-1j * omega * np.arange(0, M)))
    H = sum_b / (1 + sum_a)
    return H
