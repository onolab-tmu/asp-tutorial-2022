import numpy as np
import matplotlib.pyplot as plt

sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
x = np.random.rand(round(sec * sr))  # ホワイトノイズの生成

plt.xlim(0, 0.03)
plt.plot(t, x)
plt.savefig("outputs/05.pdf")
plt.show()

print("success!")
