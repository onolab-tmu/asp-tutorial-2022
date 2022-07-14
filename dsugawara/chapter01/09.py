# 8.で作成した関数を用いて，6.と同様にホワイトノイズと正弦波の混合信号を作成せよ．ただし，SN 比が 6dB となるようにすること．

import numpy as np
import soundfile


def make_noise(signal, is_SNR):
    noise = np.random.rand(len(signal))

    noise = noise / np.sqrt(np.sum(noise**2))
    noise = noise * np.sqrt(np.sum(signal**2))
    noise = noise * 10 ** (-1 * is_SNR / 20)

    return noise


A = 1.0
f = 440.0
sf = 16000
sec = 1.0
t = np.arange(0, sec, 1 / sf)
signal = A * np.sin(2 * np.pi * f * t)

white_noise = make_noise(signal, 6.0)

x = signal + white_noise


soundfile.write(file="09py_mixed.wav", data=x, samplerate=sf)
