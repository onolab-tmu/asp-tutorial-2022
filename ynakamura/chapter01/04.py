import numpy as np
import wavio


fs = 16000
sec = 3
fin = 660
t = np.linspace(0., sec, int(fs * sec))

y = np.sin(2.0 * np.pi * fin * t)

fin = 440

x = np.sin(2.0 * np.pi * fin * t)

mix = np.array([x, y]).T

wavio.write("sin_fin440_fin_660_fs16k.wav", mix[:, :], fs, sampwidth=2)