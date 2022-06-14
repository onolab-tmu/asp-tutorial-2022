import numpy as np
import wavio


wav = wavio.read("sin_fin440_fs16k.wav")
wavio.write("sin_fin440_fs8k.wav", wav.data[0::2], int(wav.rate / 2), sampwidth=2)