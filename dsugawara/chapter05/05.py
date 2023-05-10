import numpy as np


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
        ndarray: x[n]のSTFT

    """
    x_cut = frame_cut(L, S, x)
    T = x_cut.shape[0]
    X = np.empty((L // 2 + 1, T), dtype="complex")

    for t in range(0, T):
        x_cut[t] = x_cut[t] * win
        X[:, t] = np.fft.rfft(x_cut[t])

    return X


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


# main
A = 1.0
fs = 16000
sec = 5

nA = A * np.random.rand(round(fs * sec))
nB = A * np.random.rand(round(fs * sec))

L = 512  # 窓長
S = 256  # シフト幅
win = np.hanning(L)  # 窓関数

nA_stft = stft(L, S, nA, win)
nB_stft = stft(L, S, nB, win)

R = scm(np.array([nA_stft, nB_stft]))

print(R[100].real)
