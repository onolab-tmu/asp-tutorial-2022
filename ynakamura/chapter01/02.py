import numpy as np
import wavio


fs = 16000
sec = 3
fin = 440
t = np.linspace(0.0, sec, int(fs * sec))

x = np.sin(2.0 * np.pi * fin * t)

wavio.write("sin_fin440_fs16k.wav", x, fs, sampwidth=2)
