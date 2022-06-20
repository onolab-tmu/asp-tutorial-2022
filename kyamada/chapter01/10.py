import numpy as np
import matplotlib.pyplot as plt


def create_sinusoid(
    fs=16000,
    f=440,
    r=1,
    theta=0,
    time=3,
):
    """
    Create a sinusoid wave
    Input:
        fs: sampling frequency
        f: frequency
        r: amplitude
        theta: phase
        time: time
    Output:
        t: time_data
        x: wave data
    """
    t = np.arange(0, time, 1/fs)
    x = r * np.sin(2 * np.pi * f * t + theta)

    return t, x


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
    noise = np.random.randn(len(x))
    # 混合をする
    noise = noise / np.sqrt(np.sum(noise ** 2))  # エネルギーの正規化
    noise = noise * np.sqrt(np.sum(x ** 2))
    noise = noise * 10 ** (-snr / 20)

    return noise


def create_snr_sinusoid(
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
    #x = create_sinusoid(x)
    noise = create_snr_noise(x, snr=snr)
    x_noise = x + noise
    return x_noise


def five_point_average_filter(x):
    """
    5-point average filter
    Input:
        x: wave data
    Output:
        y: filtered wave data
    """
    y = np.zeros(len(x)-5)
    for i in range(len(x)-5):
        y[i] = np.mean(x[i-3:i+3])
    return y


if __name__ == '__main__':
    np.random.seed(0)  # シード値
    time = 0.01
    fs = 16000
    time = 3
    t, x = create_sinusoid()
    x_noise = create_snr_sinusoid(x, snr=6)
    y = five_point_average_filter(x)
    plt.plot(t, x_noise)
    plt.plot(t[0:len(y)], y)
    plt.xlim([0, 0.03])
    plt.show()
