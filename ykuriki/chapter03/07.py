import numpy as np


# 関数
def clc_diff_eq(a, b, x, length):
    """差分方程式を計算する

    Args:
        a (ndarray): yの係数（1次元配列）
        b (ndarray): xの係数（1次元配列）
        x (ndarray): 信号（1次元配列）
        length (int): yの長さ


    Returns:
        y (ndarray): 結果（1次元配列）

    """
    N = len(a)
    M = len(b)
    L = len(x)
    y = np.zeros(length)

    # bxを計算しておく
    for n in range(length):
        for k in range(M):
            if k <= n and n - k < L:
                y[n] += b[k] * x[n - k]

    for n in range(length):
        for k in range(1, N):
            if k <= n:
                y[n] -= a[k] * y[n - k]
        y[n] /= a[0]

    return y
