import numpy as np


def pad(x, L, S):
    x_pad = np.pad(x, [L - S, L - S])
    re = np.mod(len(x_pad), S)
    if re != 0:
        x_pad = np.pad(x_pad, [0, S - re])
    return x_pad


def frame_div(x, L, S):
    x_pad = pad(x, L, S)
    T = int(np.floor((len(x_pad) - L) / S)) + 1
    x_t = np.zeros((T, L))
    for t in range(T):
        x_t[t] = x_pad[t * S : t * S + L]
    return x_t


def stft(x, L, S, wnd):
    x_t = frame_div(x, L, S)
    T = len(x_t)
    X = np.zeros((T, L // 2 + 1), dtype="complex")
    for t in range(T):
        X[t] = np.fft.rfft(x_t[t] * wnd)
    return X.T


def calc_spatial_correlation_matrix(X):
    M, F, T = X.shape
    R = []
    for f in range(F):
        sum = np.zeros((M, M), dtype="complex")
        for t in range(T):
            sum += X[:, f, t].reshape(-1, 1) @ np.conj(X[:, f, t]).reshape(-1, 1).T
        R.append(1 / T * sum)
    R = np.array(R)

    return R


sec = 5.0  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
x1 = np.random.rand(round(sec * sr))  # ホワイトノイズの生成
x2 = np.random.rand(round(sec * sr))  # ホワイトノイズの生成

L = 512
S = 256
wnd = np.hanning(L)
x = np.stack([stft(x1, L, S, wnd), stft(x2, L, S, wnd)])

R = calc_spatial_correlation_matrix(x)
print(R[100])

print("success!")
