# ホワイトノイズをサンプリング周波数 16kHz で 3 秒分作成しプロットせよ．
import numpy as np
import matplotlib.pyplot as plt
import soundfile


A = 1.0
sec = 3.0
sf = 16000
t = np.arange(0, 3, 1/sf)

white_noise = A * np.random.rand(round(sf*sec))

soundfile.write(file="05py_whitenoise.wav", data=white_noise, samplerate=sf)

plt.plot(t, white_noise)
plt.xlim(0, 0.03)
plt.savefig("05py_whitenoise.png")