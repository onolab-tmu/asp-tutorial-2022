import numpy as np
import soundfile as sf

A = 1  # 振幅
f = 660  # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y1 = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成

y2, sr = sf.read("outputs/02.wav")
s = np.vstack((y1, y2)).T

sf.write("outputs/04.wav", s, sr, format="WAV", subtype="PCM_16")

print("success!")
