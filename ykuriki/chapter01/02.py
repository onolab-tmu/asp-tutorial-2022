import numpy as np
import wave


# パラメータ
fs = 16000
f = 440
r = 1
time = 3

t = np.arange(0, fs * time) / fs
sig = r * np.sin(f * 2 * np.pi * t)

# 音声ファイル出力
output = (sig * np.iinfo(np.int16).max).astype(np.int16)
wav = wave.open("./02.wav", "wb")
wav.setnchannels(1)
wav.setsampwidth(2)
wav.setframerate(fs)
wav.writeframes(output)
wav.close()
