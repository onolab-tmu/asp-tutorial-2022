import numpy as np


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


X_1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
X_2 = np.array([[4, -2 * 1j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
X = np.stack([X_1, X_2])
R = calc_spatial_correlation_matrix(X)
print(R)

print("success!")
