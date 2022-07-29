import numpy as np


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


X_1 = np.array([[1, -1j, -1, 1j], [2, -2j, -2, 2j], [3, -3j, -3, 3j]])
X_2 = np.array([[4, -2 * 1j, 1, 0], [2, -1j, 0, 0], [1, -1j, 1, 0]])
X = np.stack([X_1, X_2])

R = calc_spatial_correlation_matrix(X)
print(R)
