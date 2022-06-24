import numpy as np
import wave


# 関数
def Add_noise(s, snr):
    """SN比がn[dB]になるようにホワイトノイズを加える

    Args:
        s (ndarray): 元の信号 (float型1次元配列)
        snr (float): SN比

    Returns:
        x (ndarray): ノイズを加えた信号 (float型1次元配列)

    """
    np.random.seed(2286)

    alpha = 1 / (10 ** (snr / 20))
    noise = np.random.rand(len(s))
    noise /= np.sqrt(np.sum(noise @ noise))
    noise *= alpha * np.sqrt(np.sum(s @ s))

    x = s + noise

    return x


# パラメータ
fs = 16000
f = 440
r = 1
time = 3
snr = 6

t = np.arange(0, fs * time) / fs
sig = r * np.sin(f * 2 * np.pi * t)
x = Add_noise(sig, snr)


# 音声ファイル出力
output = (x * np.iinfo(np.int16).max).astype(np.int16)
wav = wave.open("./08.wav", "wb")
wav.setnchannels(1)
wav.setsampwidth(2)
wav.setframerate(fs)
wav.writeframes(output)
wav.close()
