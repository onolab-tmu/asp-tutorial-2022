import numpy as np


def zero_pad(x, L, S):
    x_pad = np.pad(x, L - S)
    if x_pad.shape[0] % S != 0:
        x_pad = np.pad(x_pad, ((0, S - (x_pad.shape[0] % S))))
    return x_pad


def frame_div(x, L, S):
    x_pad = zero_pad(x, L, S)
    T = (x_pad.shape[0] - L) // S
    x_div = []
    for nT in range(T):
        x_t = []
        for nL in range(L):
            x_t.append(x_pad[nT * S + nL])
        x_div.append(x_t)
    return np.array(x_div)


def stft(x, L, S, win):
    x_div = frame_div(x, L, S)
    T = x_div.shape[0]
    X = []
    for t in range(T):
        tmp = x_div[t, :]
        tmp = tmp * win
        tmp = np.fft.rfft(tmp)
        X.append(tmp)
    return np.array(X).T


def calc_spatial_correlation_matrix(X):
    M, F, T = X.shape

    x = [0] * M
    for m in range(M):
        x[m] = X[m, :, :]
    x = np.array(x)

    R = []
    for f in range(F):
        sum = np.zeros((M, M)).astype(np.complex128)
        for t in range(T):
            tmp1 = x[:, f, t].reshape(-1, 1)
            tmp2 = np.conj(x[:, f, t]).reshape(-1, 1).T
            tmp3 = tmp1 @ tmp2
            sum += tmp3
        R.append(1 / T * sum)
    R = np.array(R)

    return R


fs = 16000
sec = 5

white_noise1 = 2 * np.random.randn(fs * sec) - 1
white_noise2 = 2 * np.random.randn(fs * sec) - 1

L = 512
S = 256
win = np.hanning(L)

White_noise1 = stft(white_noise1, L, S, win)
White_noise2 = stft(white_noise2, L, S, win)
White_noise = np.stack([White_noise1, White_noise2])

R = calc_spatial_correlation_matrix(White_noise)
print(R[100, :, :].real)
