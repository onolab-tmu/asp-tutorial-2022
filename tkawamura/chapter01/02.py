# WAV ファイルの作成（モノラル）: 1.で作成した正弦波を 16bit PCM フォーマットで wav ファイルとして保存せよ．

import numpy as np
import soundfile as sf


def main():
    amp = 1  # amplitude of sine wave
    freq = 440  # frequency of sine wave (Hz)
    fs = 16000  # sampling frequency (Hz)
    sig_len = 3  # signal length (sec.)

    filename = "sin.wav"

    t = np.arange(fs * sig_len) / fs  # time
    sin_wave = amp * np.sin(2 * np.pi * freq * t)  # Asin(2πft)

    # save
    sf.write(filename, sin_wave, fs, "PCM_16")

    # 確認方法 (soundfile.info: https://pysoundfile.readthedocs.io/en/latest/#soundfile.info)
    # dtype2 = sf.info(filename)
    # print(f"information : {dtype2}")


if __name__ == "__main__":
    main()
