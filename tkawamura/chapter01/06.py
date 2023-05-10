# SN比: 信号長の等しい2個の信号 s[n], x[n] (n = 0, ..., N-1)の信号対雑音比 (SN比) を計算する関数を実装せよ．

# from .01 import make_sin_wave  # invalid syntax
import numpy as np


def calculate_snr(s, x):
    """Calculate signal to noise ratio (SNR)

    Parameters
    ----------
    s : array-like
        Signal
    x : array-like
        Noise signal

    Returns
    -------
    snr : float
        Signal to noise ratio (SNR)
    """

    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)

    return 10 * np.log10(pow_s / pow_x)


def main():
    # 確認方法 (SNRから振幅を逆算して計算が正しいか確認する)
    # amp1 = 1  # amplitude of sine wave
    # amp2 = 10  # amplitude of sine wave
    # freq = 440  # frequency of sine wave (Hz)
    # fs = 16000  # sampling frequency (Hz)
    # sig_len = 3  # signal length (sec.)

    # t = np.arange(fs * sig_len) / fs  # time
    # s = amp1 * np.sin(2 * np.pi * freq * t)  # sin(2πft)
    # x = amp2 * np.sin(2 * np.pi * freq * t)  # 10 sin(2πft)

    # print(f"SNR: {calculate_snr(s, s)} (dB)")  # 同じ振幅だと0 (dB)
    # print(f"SNR: {calculate_snr(s, x)} (dB)")  # xの振幅がsの10倍なので-20 (dB)
    return 0


if __name__ == "__main__":
    main()
