import numpy as np


def frequency_response(a, b, f, fs):
    """
    周波数応答を計算する
    Args:
        a (ndarray): y の係数
        b (ndarray): x の係数
        f (float): 周波数
        fs (float): サンプリング周波数
    Returns:
        H (ndarray): 周波数応答
    """
    omega = 2 + np.pi * f / fs
    sum_a = np.sum(a * np.exp(-1j * omega * np.arange(1, len(a))))
    sum_b = np.sum(b * np.exp(-1j * omega * np.arange(0, len(b))))
    H = sum_b / (1 + sum_a)
    return H
