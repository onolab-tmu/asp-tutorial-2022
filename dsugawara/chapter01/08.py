# SN 比を任意の値に設定できるようにホワイトノイズの振幅を調整する関数を実装せよ．

import numpy as np


def make_noise(signal, is_SNR, sf):
    noise = np.random.rand(signal.shape)

    noise = noise / np.sqrt(np.sum(noise**2))
    noise = noise * np.sqrt(np.sum(signal**2))
    noise = noise * 10 ** (-1 * is_SNR / 20)

    return noise
