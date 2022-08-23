import numpy as np
import matplotlib.pyplot as plt


# Function to adjust the amplitude of white noise to match the SNR
def adjust_snr(s, x, snr):
    return (x / np.sqrt(np.sum(x**2))) * np.sqrt(np.sum(s**2)) * 10 ** (-snr / 20)


A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 1  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成
x = np.random.rand(round(sr))  # ホワイトノイズの生成
N = sr * sec
adj_x = adjust_snr(y, x, 10)

x_1 = y + adj_x
x_2 = np.zeros(N)
for n in range(N):
    x_2[n] = y[n - 10] + adj_x[n]
x_3 = np.zeros(N)
for n in range(N):
    x_3[n] = y[n - 20] + adj_x[n]

plt.plot(t, x_1, label="x1")
plt.plot(t, x_2, label="x2")
plt.plot(t, x_3, label="x3")
plt.xlabel("time [sec]")
plt.ylabel("amplitude")
plt.xlim(0, 0.01)
plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=1, fontsize=18)
plt.grid()
plt.tight_layout()
plt.savefig("outputs/06.pdf")
plt.show()

print("success!")
