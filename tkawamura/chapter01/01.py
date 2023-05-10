# 正弦波の生成: 振幅 1, 周波数 440 Hz の正弦波をサンプリング周波数 16000 Hz で 3 秒分作成しプロットせよ．

import matplotlib.pyplot as plt
import numpy as np


def make_sin_wave(amp, freq, fs, sig_len):
    """Make sine wave

    Parameters
    ----------
    amp : int
        Amplitude of sine wave
    freq : str
        Frequency of sine wave (Hz)
    fs : str
        Sampling frequency (Hz)
    sig_len : int
        Signal length (sec.)

    Returns
    -------
    signal : array-like
        Sine wave signal
    """

    t = np.arange(fs * sig_len) / fs  # time
    sin_wave = amp * np.sin(2 * np.pi * freq * t)  # Asin(2πft)

    return sin_wave


def main():
    amp = 1  # amplitude of sine wave
    freq = 440  # frequency of sine wave (Hz)
    fs = 16000  # sampling frequency (Hz)
    sig_len = 3  # signal length (sec.)

    t = np.arange(fs * sig_len) / fs  # time
    sin_wave = make_sin_wave(amp, freq, fs, sig_len)

    # plot
    plt.title("Sine wave")
    plt.plot(t, sin_wave)
    plt.ylabel("Amplitude")
    plt.xlabel("Time (sec.)")
    # plt.xlim(0, 1 / freq)  # 確認方法 (1周期の範囲を描画)
    plt.show()


if __name__ == "__main__":
    main()
