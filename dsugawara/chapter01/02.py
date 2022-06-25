# 1.で作成した正弦波を 16bit PCM フォーマットで wav ファイルとして保存せよ．

import numpy as np
import matplotlib.pyplot as plt
import soundfile


A = 1.0
f = 440.0
sf = 16000
sec = 3.0

t = np.arange(0, sec, 1 / sf)

y = A * np.sin(2 * np.pi * f * t)

soundfile.write(
    file="02py_sin.wav", data=y, samplerate=sf, format="WAV", subtype="PCM_16"
)
