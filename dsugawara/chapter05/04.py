import numpy as np


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
X1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
X2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
X = np.array([X1, X2])

print(scm(X))
