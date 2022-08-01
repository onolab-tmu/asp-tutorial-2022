import numpy as np
import matplotlib.pyplot as plt


def make_noise(signal, is_SNR):

    """SNRを調整した雑音を生成する

    Args:
        signal (ndarray): 信号（1次元配列）
        is_SNR (double): SNR

    Return:
        ndarray: 雑音

    """
    noise = np.random.randn(len(signal))

    noise = noise / np.sqrt(np.sum(noise**2))
    noise = noise * np.sqrt(np.sum(signal**2))
    noise = noise * 10 ** (-1 * is_SNR / 20)

    return noise


def padding(L, S, x):

    """x[n]に零する詰めをする

    Args:
        L (int): 窓幅
        S (int): シフト幅
        x (ndarray): 信号（1次元配列）

    Return:
        ndarray: 零詰めされた信号

    """
    x = np.pad(x, [L - S, L - S])
    temp = S - (x.size % S)  # 末尾に詰める0の個数を求める
    if x.size % S != 0:
        x = np.pad(x, [0, temp])
    return x


def frame_cut(L, S, x):

    """x[n]をフレーム分割する

    Args:
        L (int): 窓幅
        S (int): シフト幅
        x (ndarray): 信号（1次元配列）

    Returns:
        ndarray: フレーム分割された信号

    """
    x = padding(L, S, x)
    T = (x.size - L) // S + 1
    xt = np.zeros((T, L), dtype=complex)
    for t in range(T):
        for l in range(L):
            xt[t][l] = x[t * S + l]

    return xt


def stft(L, S, x, win):

    """x[n]のSTFTを計算する

    Args:
        L (int): 窓幅
        S (int): シフト幅
        x (ndarray): 信号（1次元配列）
        win (ndarray): 窓関数（1次元配列）

    Returns:
        ndarray: x[n]のSTFT（ (L//2+1)*T の2次元配列）

    """
    x_cut = frame_cut(L, S, x)
    T = x_cut.shape[0]
    X = np.empty((L // 2 + 1, T), dtype="complex")

    for t in range(0, T):
        x_cut[t] = x_cut[t] * win
        X[:, t] = np.fft.rfft(x_cut[t])

    return X


def linear_array_vector(d, M, theta, f):

    """直線状アレイのアレイマニフォールドベクトルを求める

    Args:
        d (double): アレイ間隔
        M (int): マイク数
        theta (int): 音源方向（y軸から反時計回りが正の向き）
        f (int): 周波数

    Return:
        ndarray: アレイマニフォールドベクトル

    """
    c = 334.0
    theta = np.pi / 2 + 2 * np.pi * (theta / 360)
    u = np.array([np.sin(theta), np.cos(theta), 0]).T

    p = np.zeros([M, 3])
    for m in range(1, M + 1):
        idx_m = m - 1
        p[idx_m, 0] = ((m - 1) - (M - 1) / 2) * d
    p = p.T
    a = np.empty([u.T.shape[0], p.shape[1]], dtype="complex")  # 　a[1, M]になるはず
    a = np.exp(2j * np.pi * f / c * np.dot(u.T, p))

    return a


def scm(X):

    """空間相関行列（spatial correation matrix）を求める

    Args:
        X (ndarray): 複素数行列（3次元配列）

    Return:
        ndarray: 空間相関行列

    """
    M = X.shape[0]
    F = X.shape[1]
    T = X.shape[2]

    R = np.empty([F, M, M], dtype="complex")
    x = np.empty(M, dtype="complex")
    for f in range(0, F):
        for t in range(0, T):
            sigma = 0
            for m in range(1, M + 1):
                idx_m = m - 1
                x[idx_m] = X[idx_m, f, t]
            x[idx_m].T
            x_H = np.conjugate(x.T)
            sigma += np.dot(x, x_H)
        R[f] = 1 / T * sigma

    return R


def spatial_spectrum(z):

    M = z.shape[0]

    L = 1024
    S = 512
    F = L // 2 + 1
    win = np.hanning(L)

    Z = []
    for m in range(0, M):
        Zm = stft(L, S, z[m, :], win)
        Z.append(Zm)
    Z = np.array(Z)

    R = scm(Z)

    F = Z.shape[1]
    w = np.empty([F, 360, M], dtype="complex")
    for f in range(0, F):
        for theta in range(0, 360):
            w[f, theta, :] = linear_array_vector(0.05, M, theta, f)

    P = np.empty([F, 360], dtype="complex")
    for f in range(0, F):
        for theta in range(0, 360):
            P[f, theta] = np.conjugate(w[f, theta, :]).T @ R[f, :, :] @ w[f, theta, :]

    for f in range(21, 30):
        plt.subplot()
        plt.plot(np.arange(0, 360), 20 * np.log10(np.abs(P[f, :])))
        plt.savefig(f"10py_f={f}.png")


# main
M = 3
d = 0.05

A = 1.0
fs = 16000
sec = 1
f = 440
t = np.arange(0, fs * sec) / fs

s = A * np.sin(2 * np.pi * f * t)

noise = make_noise(s, 10)

x1 = s + noise
s2 = np.pad(s, [10, 0])
x2 = s2[0 : len(s2) - 10] + noise
s3 = np.pad(s, [20, 0])
x3 = s3[0 : len(s3) - 20] + noise

z = np.stack([x1, x2, x3])

spatial_spectrum(z)
