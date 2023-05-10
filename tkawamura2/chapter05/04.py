import numpy as np


def spa_corr(X):
    X_ = X.transpose(1, 0, 2)
    X_conj = np.conj(X_.transpose(0, 2, 1))
    return np.einsum("nft, ntk -> nfk", X_, X_conj)


X = np.array([[[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]],
              [[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]]])
print(spa_corr(X))
