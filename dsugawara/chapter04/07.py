import numpy as np
import matplotlib.pyplot as plt


def padding(L, S, x):

    x = np.pad(x, [L - S, L - S])
    temp = S - (x.size % S)  # 末尾に詰める0の個数を求める
    x = np.pad(x, [0, temp])
    return x


def frame_cut(L, S, x):
    N = x.size
    T = ((N - L) // S) + 1  # フレーム数．後で確認
    x_cut = np.empty([T, L])  # 出力
    x_pad = padding(L, S, x)
    for t in range(0, T):
        x_cut[t] = x_pad[t * S : t * S + L]
    return x_cut


def stft(L, S, x):
    x_cut = frame_cut(L, S, x)
    T = x_cut.shape[0]
    win = np.hamming(L)
    X = np.empty((L // 2 + 1, T), dtype="complex")

    for t in range(0, T):
        X[:, t] = np.fft.rfft(win * x_cut[t, :])

    return X


def optimal_window(S, win):

    L = win.size
    Q = L // S
    for l in range(0, L):
        sigma = 0
        for m in range(0, Q):
            sigma += win[l - m * S] ** 2
    win_s = win / sigma

    return win_s


def istft(S, X):
    F = X.shape[0]
    T = X.shape[1]
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    win = np.hamming(N)
    win_opt = optimal_window(S, win)
    x = np.zeros(M)
    z = np.empty((T, N))

    for t in range(0, T):
        for n in range(0, N):
            z[t, n] = np.fft.irfft(X[:, t])[n]
            x[t * S + n] += win_opt[n] * z[t, n]

    return x


# main
A = 1
f = 440
sf = 16000
sec = 0.1
t = np.arange(0, (sec * sf)) / sf
y = A * np.sin(2 * np.pi * t * f)

L = 1000  # 窓幅
S = 500  # シフト幅

Y = stft(L, S, y)

y_istft = istft(S, Y)

print(y_istft)

# plot
plt.plot(y_istft)
plt.savefig("07py_istft.png")
