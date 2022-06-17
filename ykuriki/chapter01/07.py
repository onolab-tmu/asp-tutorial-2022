import numpy as np


def Add_noise(s, snr):
    """SN比がn[dB]になるようにホワイトノイズを加える

    Args:
        s (ndarray): 元の信号 (float型1次元配列)
        snr (float): SN比

    Returns:
        x (ndarray): ノイズを加えた信号 (float型1次元配列)

    """
    np.random.seed(2286)

    alpha = 1 / (10 ** (snr / 20))
    noise = np.random.rand(len(s))
    noise /= np.sqrt(np.sum(noise @ noise))
    noise *= alpha * np.sqrt(np.sum(s @ s))

    x = s + noise

    return x
