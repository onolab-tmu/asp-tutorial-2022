import numpy as np
from scipy.io.wavfile import write

A = 1
f = 440.0
sec = 3.0
fs = 16000

t = np.arange(0, sec, 1 / fs)
y = A * np.sin(2 * np.pi * f * t)

writefilename = "02_out.wav"

y = y * 100

wav = y.astype(np.int16)
print(wav)
write(writefilename, fs, wav)
