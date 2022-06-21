import numpy as np

#SNR計算
def cal_sn(s, x):
    snr = 10 * np.log10(np.sum(s * s) / np.sum(x * x))

    return snr

#確認用
A = 1    #振幅
f = 440
sec = 3  #信号の長さ
fs = 16000 #サンプリング周波数

x = 2 * A * (np.random.rand(round(fs*sec)) - 0.5) #ホワイトノイズの生成

t = np.arange(0, sec, 1/fs) #時間インデックス

s = A * np.sin(2 * np.pi * f * t) #正弦波

print(cal_sn(s, x))

