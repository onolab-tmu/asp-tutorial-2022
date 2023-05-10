# SN比を指定した信号の混合（確認）: 8.で実装した関数を用いて，6.と同様にホワイトノイズと正弦波の混合信号を作成しwavファイルとして保存せよ．ただし，SN比が6dBとなるようにすること．


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


def calculate_amplitude_from_snr(s, x, snr):
    """Calculate signal to noise ratio (SNR)

    Parameters
    ----------
    s : array-like
        Signal
    x : array-like
        Noise signal
    snr: float
        所望のSN比 (入力SNRとも呼ぶ)

    Returns
    -------
    coef : float
        coefficient
    """

    # メモ: SNR = 10 * np.log10(pow_s / (pow_x * coef**2))
    pow_s = np.sum(s**2)
    pow_x = np.sum(x**2)

    coef = np.sqrt(pow_s / pow_x / 10 ** (snr / 10))
    return coef


def add_white_noise_with_snr(s, snr):
    white_noise = np.random.rand(len(s))  # sと同じサイズのホワイトノイズ
    coef = calculate_amplitude_from_snr(s, white_noise, snr)

    return s + coef * white_noise


def main():
    amp = 1  # amplitude of sine wave
    freq = 440  # frequency of sine wave (Hz)
    fs = 16000  # sampling frequency (Hz)
    sig_len = 3  # signal length (sec.)

    snr = 6  # 所望のSNR
    filename = "mixture.wav"

    t = np.arange(fs * sig_len) / fs  # time
    sin_wave = amp * np.sin(2 * np.pi * freq * t)  # Asin(2πft)

    mixture = add_white_noise_with_snr(sin_wave, snr)

    # save
    sf.write(filename, mixture, fs, subtype="FLOAT")  # PCMでないことに注意

    # 確認方法 (SNRを計算する)
    # mixture2, sr2 = sf.read(filename)  # 書き出したファイルの読み込み
    # white_noise = mixture2 - sin_wave  # 足し合わされたホワイトノイズ
    # print(f"SNR: {calculate_snr(sin_wave, white_noise)} (dB)")


if __name__ == "__main__":
    main()
