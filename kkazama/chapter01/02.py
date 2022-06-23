from wsgiref.headers import tspecials
import numpy as np
import soundfile as sf

A = 1
f = 440
sec = 3
fs = 16000

t = np.arange(0, sec, 1/fs)

xt = A * np.sin(2 * np.pi * f * t)

sf.write(file = "sin.wav", data = xt, samplerate = fs, format = "WAV", subtype = "PCM_16")