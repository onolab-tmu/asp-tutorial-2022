import numpy as np


def circular_array_vector(r, M, theta, f):

    """円状アレイのアレイマニフォールドベクトルを求める

    Args:
        r (double): アレイ半径
        M (int): マイク数
        theta (int): 音源方向（y軸から反時計回りが正の向き）
        f (int): 周波数

    Return:
        ndarray: アレイマニフォールドベクトル

    """
    c = 334.0
    theta = np.pi / 2 + 2 * np.pi * (theta / 360)
    u = np.array([np.sin(theta), np.cos(theta), 0]).T

    p = np.zeros([M, 3])
    for m in range(1, M + 1):
        idx_m = m - 1
        p[idx_m, 0] = r * np.sin(2 * np.pi / M * (m - 1))
        p[idx_m, 1] = r * np.cos(2 * np.pi / M * (m - 1))
    p = p.T
    a = np.empty([u.T.shape[0], p.shape[1]], dtype="complex")  # 　a[1, M]になるはず
    a = np.exp(2j * np.pi * f / c * np.dot(u.T, p))

    return a


# main
r = 0.05
M = 3
theta = 45
f = 1000

print(circular_array_vector(r, M, theta, f))
