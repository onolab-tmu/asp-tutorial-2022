import numpy as np
import matplotlib.pyplot as plt


def create_snr_noise(
    x,
    snr
):
    """
    Create a sinusoid wave with SNR
    Input:
        x: wave data
        snr: SNR
    Output:
        noise: noise data
    """
    # ホワイトノイズの作成
    noise = np.random.randn(len(t))
    # 混合をする
    noise = noise / np.sqrt(np.sum(noise ** 2))  # エネルギーの正規化
    noise = noise * np.sqrt(np.sum(x ** 2))
    noise = noise * 10 ** (-snr / 20)

    return noise


if __name__ == '__main__':
    np.random.seed(0)  # シード値
    time = 0.01
    fs = 16000
    t = np.arange(0, time, 1/fs)
    x = 1000 * np.sin(2 * np.pi * 440 * t)
    noise = create_snr_noise(x, snr=10)
    plt.plot(t, noise)
    plt.show()
