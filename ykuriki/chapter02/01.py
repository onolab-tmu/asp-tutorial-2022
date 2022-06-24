import numpy as np


# 関数
def clc_dft(x):
    """x[n]の離散フーリエ変換(DFT)を計算する

    Args:
        x (ndarray): 信号 (float型1次元配列)

    Returns:
        X (ndarray): 信号のDFT (complex型1次元配列)

    """
    N = len(x)
    n = np.arange(N)
    X = np.zeros(N, dtype="complex64")

    for k in range(N):
        X[k] = np.sum(x[n] * np.exp(-2j * np.pi * k * n / N))

    return X


def clc_idft(X):
    """X[n]の逆離散フーリエ変換(IDFT)を計算する

    Args:
        X (ndarray): 信号 (complex型1次元配列)

    Returns:
        x (ndarray): 信号のIDFT (float型1次元配列)

    """
    N = len(X)
    k = np.arange(N)
    x = np.zeros(N, dtype="float64")

    for n in range(N):
        x[n] = np.sum(X[k] * np.exp(2j * np.pi * k * n / N)) / N

    return x
