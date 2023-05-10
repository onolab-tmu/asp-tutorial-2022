# 簡単なフィルタ処理: 9.の信号に対して5点移動平均フィルタを適用した結果と元の信号をプロットせよ．

import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf


# 確認用．06.pyで作成
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


# https://github.com/onolab-tmu/morise-asa/blob/main/tkawamura/chapter02/07.pyより
def moving_average(x, M):
    """M-point moving average

    Parameters
    ----------
    x : array-like
        Signal
    M : int
        Filter length

    Returns
    -------
    y : array-like
        Moving averaged signal
    """

    _M = int(M // 2)
    y = np.zeros((len(x), 1))  # length は　len sizeなどに変換
    for i in [i for i in range(_M, len(y) - _M + 1)]:
        y[i] = np.mean(x[i - _M : i + _M])

    return y


def main():
    filename = "mixture_down.wav"
    filter_length = 5

    noisy, fs = sf.read(filename)  # 書き出したファイルの読み込み
    # print(f"sampling rage: {fs} (Hz)")

    enhanced = moving_average(noisy, filter_length).squeeze()

    # plot
    t = np.arange(len(noisy)) / fs
    plt.title(f"{filter_length}-point moving average")
    plt.plot(t, noisy, label="Noisy")
    plt.plot(t, enhanced, label="Enhanced")
    # plt.xlim(0, 100 / fs)  # 確認
    plt.legend()
    plt.show()

    # 確認 (SNRを見る)

    # # clean信号 (08.pyファイルを作成した時と同じ条件)
    # amp = 1  # amplitude of sine wave
    # freq = 440  # frequency of sine wave (Hz)
    # fs = 16000  # sampling frequency (Hz)
    # sig_len = 3  # signal length (sec.)

    # t = np.arange(fs * sig_len) / fs  # time
    # clean = amp * np.sin(2 * np.pi * freq * t)  # Asin(2πft)
    # t_down = t[::2]
    # clean_down = clean[::2]

    # noise = noisy - clean_down
    # noise_enhanced = enhanced - clean_down

    # print(calculate_snr(clean_down[filter_length:], noise[filter_length:]))
    # print(calculate_snr(clean_down[filter_length:], noise_enhanced[filter_length:]))

    # 確認 (残留雑音信号のplot)
    # plt.title(f"{filter_length}-point moving average")
    # plt.plot(t_down[filter_length:], (noisy - clean_down)[filter_length:], label="Noisy")
    # plt.plot(t_down[filter_length:], (enhanced - clean_down)[filter_length:], label="Enhanced")
    # plt.xlim(0, 100 / fs)  # 確認
    # plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()
