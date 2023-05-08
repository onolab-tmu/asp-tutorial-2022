# 信号の混合: 1.で作成した正弦波と 4.で作成したホワイトノイズと正弦波を混合してプロットせよ．
import matplotlib.pyplot as plt
import numpy as np


def main():
    # 2つの信号に共通の全パラメータ
    fs = 16000  # sampling frequency (Hz)
    sig_len = 3  # signal length (sec.)

    # 1.で作成した正弦波のパラメータ
    amp = 1  # amplitude of sine wave
    freq = 440  # frequency of sine wave (Hz)

    t = np.arange(fs * sig_len) / fs  # time
    sin_wave = amp * np.sin(2 * np.pi * freq * t)  # 1.で作成した正弦波
    white_noise = np.random.rand(fs * sig_len)  # 4.で作成したホワイトノイズ
    mixture = sin_wave + white_noise

    # plot
    plt.title("Mixture")
    plt.plot(t, mixture, label="Mixture")
    # plt.plot(t, sin_wave, marker=".", label="Sine wave")  # 確認用
    # plt.plot(t, white_noise, marker=".", label="White noise")  # 確認用
    plt.ylabel("Amplitude")
    plt.xlabel("Time (sec.)")
    # plt.xlim(0, 10 / fs)  # 確認方法: 10サンプル分だけ表示
    # plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
