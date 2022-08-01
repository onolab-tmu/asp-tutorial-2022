import numpy as np


def array_vector(crd, theta, f):

    """アレイの座標からアレイマニフォールドベクトルを求める

    Args:
        crd (ndarray): アレイの座標（3次元配列）
        theta (int): 音源方向（y軸から反時計回りが正の向き）
        f (int): 周波数

    Return:
        ndarray: アレイマニフォールドベクトル

    """
    M = crd.shape[0]
    c = 334.0
    theta = np.pi / 2 + 2 * np.pi * (theta / 360)
    u = np.array([np.sin(theta), np.cos(theta), 0]).T

    p = np.zeros([M, 3])
    for m in range(1, M + 1):
        idx_m = m - 1
        r = crd[idx_m, 0] ** 2 + crd[idx_m, 1] ** 2
        if r == 0:
            sin, cos = 0, 0
        else:
            sin = crd[idx_m, 1] / r
            cos = crd[idx_m, 0] / r
        p[idx_m, 0] = r * sin
        p[idx_m, 1] = r * cos
    p = p.T
    a = np.empty([u.T.shape[0], p.shape[1]], dtype="complex")  # a[1, M]になるはず
    a = np.exp(2j * np.pi * f / c * np.dot(u.T, p))

    return a


# main
d = 0.05
theta = 45
f = 1000

# 直線状アレイの確認
liner = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])
print(array_vector(liner, theta, f))

# 円状アレイの確認
r = 0.05
circular = np.array(
    [
        [r, 0, 0],
        [r * np.cos(2 * np.pi / 3), r * np.sin(2 * np.pi / 3), 0],
        [r * np.cos(2 * np.pi * 2 / 3), r * np.sin(2 * np.pi * 2 / 3), 0],
    ]
)
print(array_vector(circular, theta, f))
