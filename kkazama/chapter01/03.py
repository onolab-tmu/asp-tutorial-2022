from wsgiref.headers import tspecials
import numpy as np
import librosa
import soundfile as sf

data, sr = sf.read("sin.wav")

sr = 8000

sf.write("new_sin.wav", data, sr, subtype="PCM_16")


