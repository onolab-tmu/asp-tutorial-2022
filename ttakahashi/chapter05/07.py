import numpy as np
import matplotlib.pyplot as plt


# Function to adjust the amplitude of white noise to match the SNR
def adjust_snr(s, x, snr):
    return (x / np.sqrt(np.sum(x**2))) * np.sqrt(np.sum(s**2)) * 10 ** (-snr / 20)


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


def syn_wnd(wnd, S):
    L = len(wnd)
    Q = L // S
    swnd = np.zeros(L)
    for i in range(L):
        k = i - (Q - 1) * S
        if k < 0:
            k = 0
        swnd[i] = wnd[i] / np.sum(wnd[k : i + (Q - 1) * S] ** 2)
    return swnd


def istft(S, X):
    F, T = X.shape
    N = 2 * (F - 1)
    M = S * (T - 1) + N
    swnd = np.ones(N)
    x = np.zeros(M, dtype="complex")
    z = np.zeros((T, N), dtype="complex")
    for t in range(T):
        z[t] = np.fft.irfft(X[:, t])
        x[t * S : t * S + N] += swnd * z[t]
    return x


A = 1  # 振幅
f = 440  # 周波数 Hz
sec = 1  # 信号の長さ s
sr = 16000  # サンプリング周波数 Hz

t = np.arange(sec * sr) / sr  # サンプリング点の生成
y = A * np.sin(2 * np.pi * f * t)  # 正弦波の生成
x = np.random.rand(round(sr))  # ホワイトノイズの生成
N = sr * sec
adj_x = adjust_snr(y, x, 10)

x_1 = y + adj_x
x_2 = np.zeros(N)
for n in range(N):
    x_2[n] = y[n - 10] + adj_x[n]
x_3 = np.zeros(N)
for n in range(N):
    x_3[n] = y[n - 20] + adj_x[n]

L = 512
S = 256
wnd = np.hanning(L)
x = np.stack([stft(x_1, L, S, wnd), stft(x_2, L, S, wnd), stft(x_3, L, S, wnd)])

M, F, T = x.shape
tau = np.array([0, 10 / sr, 20 / sr])
w = np.zeros((F, M), dtype="complex")
Y = np.zeros((F, T), dtype="complex")
for f in range(F):
    for m in range(M):
        w[f, m] = 1 / M * np.exp(-1j * 2 * np.pi * f * sr / 2 / (F - 1) * tau[m])
    Y[f] = np.conj(w[f]).T @ x[:, f, :]
y = istft(S, Y)

plt.plot(np.arange(sec * y.shape[0]) / y.shape[0], y)
plt.xlabel("n")
plt.ylabel("amplitude")
plt.xlim(0, 0.1)
plt.grid()
plt.tight_layout()
plt.savefig("outputs/07.pdf")
plt.show()

print("success!")
