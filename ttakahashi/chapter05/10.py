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


def calc_vector(crd, theta, f):
    M = crd.shape[1]
    x = crd[0]
    y = crd[1]
    if len(x) != len(y):
        print("Error: The numbers x and y are not equal.")
        exit()
    c = 334
    u = np.array([np.sin(theta), np.cos(theta), 0]).T
    a = np.zeros(M, dtype="complex")
    for m in range(M):
        p_m = np.array([x[m], y[m], 0]).T
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ p_m)

    return a


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


def calc_spatial_spec(z, w):
    F, _, M = w.shape  # 周波数ビンの総数，角度の総数，マイク数

    L = 1024
    S = 512
    wnd = np.hanning(L)

    Z = [0] * M
    for m in range(M):
        Z[m] = stft(z[m], L, S, wnd)
    Z = np.array(Z)

    M, F, T = Z.shape

    R = calc_spatial_correlation_matrix(Z)

    P = np.zeros((F, 361), dtype="complex")
    for f in range(F):
        for theta in range(361):
            P[f, theta] = np.conj(w[f, theta, :]).T @ R[f, :, :] @ w[f, theta, :]

    for f in range(20, 31):
        plt.plot(np.arange(361), 20 * np.log10(np.abs(P[f, :])))
        plt.title(f"f = {f}")
        plt.xlabel("angle [deg]")
        plt.ylabel("spatial spec. [dB]")
        plt.xlim(0, 360)
        plt.ylim(0, np.max(20 * np.log10(np.abs(P))))
        plt.tight_layout()
        plt.savefig(f"outputs/10_{f}.pdf")
        plt.show()
        plt.clf()
        plt.close()


d = 0.05
M = 3
L = 1024
F = L // 2 + 1

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

x = np.stack([x_1, x_2, x_3])

crd_lin = np.zeros((3, M))
for m in range(M):
    crd_lin[0][m] = ((m - 1) - (M - 1) / 2) * d

a_lin = np.zeros((F, 361, M), dtype="complex")
for theta in range(361):
    for f in range(F):
        a_lin[f, theta, :] = calc_vector(crd_lin, theta, f)
w = a_lin / M

calc_spatial_spec(x, w)

print("success!")
