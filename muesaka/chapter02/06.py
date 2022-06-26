import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    a = 1.0  # 振幅
    sec = 3  # 信号長
    sr = 16000  # サンプリング周波数
    f = 440  # 周波数

    t = np.arange(0, sec * sr) / sr
    signal = a * np.sin(2 * np.pi * f * t)
    fft_signal = np.fft.fft(signal)
    amp_fft_signal = 20 * np.log10(np.abs(fft_signal))
    phase_fft_signal = 20 * np.log10(np.angle(fft_signal))
    freq_index = np.arange(len(fft_signal)) / len(fft_signal) * sr  # プロットのインデックス用

    fig, ax = plt.subplots(nrows=2, ncols=1)
    ax[0].plot(freq_index, amp_fft_signal)
    ax[0].set_title("amplitude")
    ax[1].plot(freq_index, phase_fft_signal)
    ax[1].set_title("phase")
    plt.tight_layout()
    plt.show()
