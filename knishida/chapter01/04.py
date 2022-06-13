import numpy as np
import soundfile as sf

A = 1
f = 440.0
f_2 = 660.0
sec = 3.0
fs = 16000
writefilename = "./knishida/chapter01/04_out.wav"

t = np.arange(0, sec, 1 / fs)
y = A * np.sin(2 * np.pi * f * t)
y_2 = A * np.sin(2 * np.pi * f_2 * t)


wav = np.array([y, y_2])
wav = wav.T

sf.write(writefilename, wav, fs, "PCM_16")
