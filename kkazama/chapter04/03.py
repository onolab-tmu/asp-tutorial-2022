import numpy as np

#ゼロ詰め
def zero_pad(x, L, S):
    x = np.pad(x, L-S, L-S)
    a = len(x) % S
    if a != 0:
        x = np.pad(x, (0, S-a))
    
    return x

#フレーム分割
def sep_frame(x, L, S):
    x = zero_pad(x, L, S)
    T = len(x) / S
    xt = np.zeros((T, L))
    for t in range(T):
        for l in range(L):
            xt[t] = x[t * S + l]

    return xt

# フーリエ変換
def sig_stft(x, L, S):
    xt = sep_frame(x, L, S)
    w = np.hamming(L)
    T = xt.shape[0]
    X = np.zeros((L // 2 + 1, T), dtype=complex)
    for t in range(T):
        xt[t] = xt[t] * w
        X[:, t] = np.fft.rfft(xt[t])

    return X

