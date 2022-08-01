import numpy as np


# 関数
def clc_amv(p, theta, f):
    """アレイマニフォールドベクトルを計算する

    Args:
        p (ndarray): アレイの座標
        theta (int/double): 音源方向 [deg]
        f (int/double): 周波数 [Hz]


    Returns:
        a (ndarray): アレイマニフォールドベクトル

    """
    c = 334
    M = len(p)
    theta = np.radians(theta)
    a = np.zeros(M, dtype="complex")
    u = np.array([np.sin(theta), np.cos(theta), 0])

    for m in range(M):
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ p[m])

    return a


d = 0.05
r = 0.05
M = 3
theta = 45
f = 1000

p_l = np.vstack([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])
print(clc_amv(p_l, theta, f))

p_c = np.vstack(
    [
        [r * np.sin(0), r * np.cos(0), 0],
        [r * np.sin(2 * np.pi / M), r * np.cos(2 * np.pi / M), 0],
        [r * np.sin(4 * np.pi / M), r * np.cos(4 * np.pi / M), 0],
    ]
)
print(clc_amv(p_c, theta, f))
