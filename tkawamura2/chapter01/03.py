import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from librosa import resample

fs, y = read("440.wav")
y_ = resample(y, fs, 8000)

write("440_8000.wav", 8000, y_)