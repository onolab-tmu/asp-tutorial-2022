import numpy as np


# 関数
def ham_wnd(N):
    """ハミング窓を生成する

    Args:
        N (int): 窓の長さ

    Returns:
        w (ndarray): ハミング窓（float型1次元配列）

    """
    n = np.arange(N)
    w = 0.54 - 0.46 * np.cos(2 * np.pi * n / (N - 1))

    return w


fs = 16000
sec = 3

wnd = ham_wnd(fs * sec)

fft_wnd = np.fft.fft(wnd)
