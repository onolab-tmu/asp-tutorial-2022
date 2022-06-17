import numpy as np

# 関数
def SNR(s, x):
    """s[n]とx[n]の信号対雑音比(SN比)を計算する

    Args:
        s (ndarray): 信号 (float型1次元配列)
        x (ndarray): ノイズ (float型1次元配列)

    Returns:
        snr (float): 信号対雑音比 (SN比)

    """
    snr = 10 * np.log10(np.sum(s @ s) / np.sum(x @ x))

    return snr
