import numpy as np
import matplotlib.pyplot as plt

#ノイズの振幅調整
def cal_adj_amp(s, x, snr):
    x = x / np.sqrt(sum(x * x))
    x = x * np.sqrt(sum(s * s))
    x = x * 10 ** (-snr / 20)

    return x

A = 1    #信号の振幅
f = 440
sec = 3  #信号の長さ
fs = 16000 #サンプリング周波数

#調整前
r = np.random.rand(round(fs*sec))
x = 2 * A * (r - 0.5) #ホワイトノイズの生成

t = np.arange(0, sec, 1/fs) #時間インデックス
s = A * np.sin(2 * np.pi * f * t) #正弦波

#調整後
x = cal_adj_amp(s, x, 6.0)

plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.plot(t, x)
plt.xlim(0, 0.03) #軸範囲

#移動平均
y = np.zeros(x.size)
M = 5

for i  in range(M+1, y.size - M):
    y[i] = np.mean(x[i - M : i + M])

plt.subplot(2, 1, 2)
plt.plot(t, s)
plt.plot(t, y)
plt.xlim(0, 0.03) #軸範囲
plt.show()