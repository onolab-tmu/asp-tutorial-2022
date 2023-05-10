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
    eps = np.random.rand(len(s))
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


def clc_amv(p, theta, f):
    """アレイマニフォールドベクトルを計算する

    Args:
        p (ndarray): アレイの座標
        theta (int/double): 音源方向 [deg]
        f (int/double): 周波数 [Hz]


    Returns:
        a (ndarray): アレイマニフォールドベクトル

    """
    c = 334
    M = len(p)
    theta = np.radians(theta)
    a = np.zeros(M, dtype="complex")
    u = np.array([np.sin(theta), np.cos(theta), 0])

    for m in range(M):
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ p[m])

    return a


def clc_sp_mat(X):
    """空間相関行列を計算する

    Args:
        X (ndarray): M個のF×T複素数行列


    Returns:
        R (ndarray): 空間相関行列

    """
    M, F, T = X.shape
    R = np.zeros((F, M, M), dtype="complex")

    for f in range(F):
        for t in range(T):
            x_ft = X[:, f, t]
            R[f] += np.outer(x_ft, np.conjugate(x_ft))
        R[f] /= T

    return R


def clc_sp_spec(z):
    """空間スペクトルを計算する

    Args:
        z (ndarray): MチャネルのN点実数値信号

    """
    M = len(z)
    L = 1024
    S = 512
    fs = 16000
    d = 0.05

    wnd = np.hanning(L)

    Z1 = clc_stft(z[0], wnd, L, S)
    F, T = Z1.shape
    Z = np.zeros((M, F, T), dtype="complex")
    Z[0] = Z1
    for m in range(1, M):
        Z[m] = clc_stft(z[m], wnd, L, S)

    R = clc_sp_mat(Z)

    p = np.vstack([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])
    P = np.zeros(361, dtype="complex")
    for f in range(20, 31):
        fq = f * (fs / 2) / (F - 1)
        for theta in range(361):
            w = clc_amv(p, theta, fq) / M
            P[theta] = np.conjugate(w) @ R[f] @ w

        plt.plot(np.arange(361), 20 * np.log10(abs(P)))
        plt.xlabel("phase [deg]")
        plt.ylabel("|P(θ)|")
        plt.title("f=" + str(f))
        plt.tight_layout()
        plt.show()

    return


fs = 16000
f = 440
r = 1
sec = 1
snr = 10


t = np.arange(0, fs * sec) / fs
s = r * np.sin(f * 2 * np.pi * t)
eps = snr_noise(s, snr)

z1 = s + eps
z2 = np.block([np.zeros(10), s[:-10]]) + eps
z3 = np.block([np.zeros(20), s[:-20]]) + eps
z = np.array([z1, z2, z3])


clc_sp_spec(z)
