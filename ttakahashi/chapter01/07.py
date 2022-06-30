import numpy as np

A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 3.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成
x = np.random.rand(round(sr))  # ホワイトノイズの生成


# Function to calculate SNR
def calc_snr(s, x):
    return 10 * np.log10(np.sum(s**2) / np.sum(x**2))


print(calc_snr(y, x))

print("success!")
