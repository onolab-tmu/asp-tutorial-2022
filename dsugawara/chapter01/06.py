# 1.で作成した正弦波と 4.で作成したホワイトノイズと正弦波を混合してプロットせよ．

import numpy as np
import matplotlib.pyplot as plt
import soundfile


y, y_samplerate = soundfile.read("02py_sin.wav")
white_noise, white_noise_samplerate = soundfile.read("05py_whitenoise.wav")

t = np.arange(0, 3, 1/y_samplerate)

y_mixed = y + white_noise
plt.xlim(0, 0.03)
plt.plot(t, y_mixed)
plt.savefig("06py_mixed.png")