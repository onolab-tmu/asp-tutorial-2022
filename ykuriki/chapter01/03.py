import numpy as np
import wave


# パラメータ
fs = 16000
f1 = 440
f2 = 660
r = 1
time = 3

t = np.arange(0, fs * time) / fs
sig1 = r * np.sin(f1 * 2 * np.pi * t)
sig2 = r * np.sin(f2 * 2 * np.pi * t)
sig = np.array([sig1, sig2]).T.reshape(-1)

# 音声ファイル出力
output = (sig * np.iinfo(np.int16).max).astype(np.int16)
wav = wave.open("./03.wav", "wb")
wav.setnchannels(2)
wav.setsampwidth(2)
wav.setframerate(fs)
wav.writeframes(output)
wav.close()
