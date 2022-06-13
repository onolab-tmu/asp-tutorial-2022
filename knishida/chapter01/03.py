import numpy as np
from scipy.io.wavfile import write, read
from scipy import signal

readfilename = "./knishida/chapter01/02_out.wav"
writefilename = "./knishida/chapter01/03_out.wav"

fs, data = read(readfilename)

data_8 = signal.decimate(data, 2)
fs_8 = 8000

wav = data_8.astype(np.int16)
write(writefilename, fs_8, wav)
