import numpy as np
# from math import ceil
import matplotlib.pyplot as plt
import librosa


def set_snr(s, snr):
    A_s = np.linalg.norm(s)
    x = np.random.randn(round(len(s)))
    x = A_s * x / (10 ** (snr / 20) * np.linalg.norm(x))
    return x


def spa_corr(X):
    X_ = X.transpose(1, 0, 2)
    X_conj = np.conj(X_.transpose(0, 2, 1))
    return np.einsum("nft, ntk -> nfk", X_, X_conj)


def spatial_spectrol(z, fs, f):
    Z = librosa.stft(z, n_fft=1024, hop_length=512, window="hann")
    R_z = spa_corr(Z)

    P = np.empty([360], dtype=np.complex128)
    for theta in range(360):
        w = np.empty([3], dtype=np.complex128)
        w = np.array([np.exp(-1j * np.pi * theta * f * 0 / 180),
                      np.exp(-1j * np.pi * theta * f * 10 / (fs * 180)),
                      np.exp(-1j * np.pi * theta * f * 20 / (fs * 180))]) / 3
        P[theta] = np.conj(w).T @ R_z[f] @ w

    plt.plot(20 * np.log(np.abs(P)))
    plt.show()


a = 1     # 振幅
fs = 16000  # サンプリング周波数
f = 440  # 周波数
sec = 1   # 秒
snr = 10

x = np.arange(sec * fs) / fs
y = np.sin(2 * x * np.pi * f)

white_noise = set_snr(y, snr)

x1 = y + white_noise
x2 = np.pad(y[:-9], (9, 0)) + white_noise
x3 = np.pad(y[:-19], (19, 0)) + white_noise
z = np.concatenate([x1.reshape([1, x1.size]), x2.reshape(
    [1, x2.size]), x3.reshape([1, x3.size])], axis=0)

spatial_spectrol(z, fs, f=13 - 1)
