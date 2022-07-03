import numpy as np
import soundfile as sf

A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成

sf.write("outputs/02.wav", y, sr, format="WAV", subtype="PCM_16")

print("success!")
