import numpy as np
import matplotlib.pyplot as plt


# 関数
def snr_noise(s, snr):
    """SN比がn[dB]になるようにホワイトノイズを設計する

    Args:
        s (ndarray): 元の信号 (float型1次元配列)
        snr (float): SN比

    Returns:
        eps (ndarray): ノイズ (float型1次元配列)

    """
    np.random.seed(2286)

    alpha = 1 / (10 ** (snr / 20))
    eps = np.random.randn(len(s))
    eps /= np.sqrt(np.sum(eps @ eps))
    eps *= alpha * np.sqrt(np.sum(s @ s))

    return eps


def zero_pad(x, L, S):
    """x[n]に零詰めする

    Args:
        x (ndarray): 信号（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: 零詰めされた信号

    """
    x = np.block([np.zeros(L - S), x, np.zeros(L - S)])

    if len(x) % S != 0:
        x = np.block([x, np.zeros(S - (len(x) % S))])

    return x


def frame_div(x, L, S):
    """x[n]をフレーム分割する

    Args:
        x (ndarray): 信号（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: フレーム分割された信号

    """
    x = zero_pad(x, L, S)
    T = int(np.floor((len(x) - L) / S)) + 1
    xt = np.zeros((T, L))

    for t in range(T):
        xt[t] = x[t * S : t * S + L]

    return xt


def clc_stft(x, w, L, S):
    """x[n]のSTFTを計算する

    Args:
        x (ndarray): 信号（1次元配列）
        w (ndarray): 窓関数（1次元配列）
        L (int): 窓幅
        S (int): シフト幅

    Returns:
        ndarray: x[n]のSTFT

    """
    x = frame_div(x, L, S)
    T = len(x)
    X = np.zeros((T, L // 2 + 1), dtype="complex")

    for t in range(T):
        X[t] = np.fft.rfft(x[t] * w)

    return X.T


def syn_wnd(w, S):
    """合成窓を生成する

    Args:
        w (ndarray): 窓関数
        S (int): シフト幅

    Returns:
        ws (ndarray): 合成窓（float型1次元配列）

    """
    L = len(w)
    Q = L // S
    ws = np.zeros(L)

    for l in range(L):
        tmp = 0
        for m in range(-Q + 1, Q):
            if l - m * S < L:
                tmp += w[l - m * S] ** 2
        ws[l] = w[l] / tmp

    return ws


def clc_istft(X, S):
    """X[f,t]のISTFTを計算する

    Args:
        X (ndarray): F×Tの複素数行列
        S (int): シフト幅

    Returns:
        x_hat (ndarray): X[f,t]のISTFT

    """
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N

    x_hat = np.zeros(M, dtype="complex")
    z = np.zeros((T, N), dtype="complex")
    ws = syn_wnd(np.hamming(N), S)

    for t in range(T):
        z[t] = np.fft.irfft(X[:, t])
        x_hat[t * S : t * S + N] += ws * z[t]

    return x_hat


def clc_dsbf(X, tau, S):
    """強調信号を計算する

    Args:
        X (ndarray): M個のF×T複素数行列
        tau (ndarray): 遅延
        S (int): シフト幅

    Returns:
        y (ndarray): 強調信号

    """
    M, F, T = X.shape
    Y = np.zeros((F, T), dtype="complex")

    for f in range(F):
        fq = f * (fs / 2) / (F - 1)
        w_f = np.exp(-1j * 2 * np.pi * fq * tau) / M
        for t in range(T):
            x_ft = X[:, f, t]
            Y[f, t] = np.conjugate(w_f) @ x_ft

    y = clc_istft(Y, S)

    return y


fs = 16000
f = 440
r = 1
sec = 1
snr = 10
L = 1024
S = 512

t = np.arange(0, fs * sec) / fs
s = r * np.sin(f * 2 * np.pi * t)
eps = snr_noise(s, snr)
w = np.hanning(L)

x1 = s + eps
x2 = np.block([np.zeros(10), s[:-10]]) + eps
x3 = np.block([np.zeros(20), s[:-20]]) + eps

X1 = clc_stft(x1, w, L, S)
X2 = clc_stft(x2, w, L, S)
X3 = clc_stft(x3, w, L, S)
X = np.array([X1, X2, X3])

tau = np.array([0, 10 / fs, 20 / fs])

y = clc_dsbf(X, tau, S)

# プロット
plt.plot(np.arange(len(y)) / fs, y)
plt.xlabel("time [sec]")
plt.ylabel("amplitude")
plt.xlim([0.1, 0.11])
plt.grid()
plt.tight_layout()

plt.show()
