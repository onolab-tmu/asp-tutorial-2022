import numpy as np
import matplotlib.pyplot as plt


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
        ndarray: x[n]のSTFT（2次元配列）

    """
    x_cut = frame_cut(L, S, x)
    T = x_cut.shape[0]
    X = np.empty((L // 2 + 1, T), dtype="complex")

    for t in range(0, T):
        x_cut[t] = x_cut[t] * win
        X[:, t] = np.fft.rfft(x_cut[t])

    return X


def optimal_window(S, win):

    """ISTFTに用いる最適化合成窓

    Args:
        S (int): シフト幅
        win (ndarray): 窓関数

    Return:
        ndarray: 最適化合成窓（1次元配列）
    """

    L = win.size
    Q = L // S
    for l in range(0, L):
        sigma = 0
        for m in range(0, Q):
            sigma += win[l - m * S] ** 2
    win_s = win / sigma

    return win_s


def istft(S, X, win):

    """X[R*I]の逆フーリエ変換を計算する

    Args:
        S (int): シフト幅
        X (ndarray): 周波数領域の信号（2次元配列）
        win (ndarray): 窓関数（1次元配列）

    Return:
        ndarray: X[R*I]のISTFT（1次元配列）
    """
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    win_opt = optimal_window(S, win)
    x = np.zeros(M)
    z = np.empty((T, N))

    for t in range(0, T):
        for n in range(0, N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] += win_opt[n] * z[t, n]

    return x


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


# main
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

# 遅延和ビームフォーマ
L = 1024  # 窓幅
S = 512  # シフト幅
win = np.hanning(L)  # 窓関数
X1 = stft(L, S, x1, win)
X2 = stft(L, S, x2, win)
X3 = stft(L, S, x3, win)
X = np.stack([X1, X2, X3])

F = X.shape[1]
T = X.shape[2]
tau = np.array([0, 10 / fs, 20 / fs])
w = np.empty([F, 3], dtype="complex")
Y = np.empty([F, T], dtype="complex")
for Fn in range(0, F):
    f = (fs / 2) / (F - 1) * Fn
    w[Fn, :] = 1 / 3 * np.exp(-2j * np.pi * f * tau)
    Y[Fn, :] = np.dot(np.conjugate(w[Fn, :].T), X[:, Fn, :])

y = istft(S, Y, win)

plt.plot(np.arange(0, sec * y.shape[0]) / fs, y)
plt.xlim(0, 0.1)
plt.savefig("07py_beamforming.png")
