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


delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])

fft_delta = np.fft.fft(delta)

# 2. の結果
dft_delta = clc_dft(delta)

# 比較
print(np.array_equal(fft_delta, dft_delta))
