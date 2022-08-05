import numpy as np
import librosa


def spa_corr(X):
    X_ = X.transpose(1, 0, 2)
    X_conj = np.conj(X_.transpose(0, 2, 1))
    return np.einsum("nft, ntk -> nfk", X_, X_conj)


white_noise = np.random.randn(2, 16000 * 5)
print(white_noise.shape)
WN = librosa.stft(white_noise, n_fft=512, hop_length=256, window="hann")
R = spa_corr(WN)
print(R[100])
