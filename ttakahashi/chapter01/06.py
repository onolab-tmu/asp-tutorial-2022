import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
x = np.random.rand(round(sec * sr))  # ホワイトノイズの生成

y, sr = sf.read("outputs/02.wav")
s = x + y

plt.xlim(0, 0.03)
plt.plot(t, s)
plt.savefig("outputs/06.pdf")
plt.show()

print("success!")
