import numpy as np


# 関数
def clc_sp_mat(X):
    """空間相関行列を計算する

    Args:
        X (ndarray): M個のF×T複素数行列


    Returns:
        R (ndarray): 空間相関行列

    """
    M, F, T = X.shape
    R = np.zeros((F, M, M), dtype="complex")

    for f in range(F):
        for t in range(T):
            x_ft = X[:, f, t]
            R[f] += np.outer(x_ft, np.conjugate(x_ft))
        R[f] /= T

    return R


X1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
X2 = np.array([[4, -2j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
X = np.array([X1, X2])

print(clc_sp_mat(X))
