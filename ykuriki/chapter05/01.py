import numpy as np


# 関数
def clc_amv_line(d, M, theta, f):
    """アレイマニフォールドベクトルを計算する

    Args:
        d (double): マイク間隔 [m]
        M (int): マイク数
        theta (int/double): 音源方向 [deg]
        f (int/double): 周波数 [Hz]


    Returns:
        a (ndarray): アレイマニフォールドベクトル

    """
    c = 334
    theta = np.radians(theta)
    a = np.zeros(M, dtype="complex")
    u = np.array([np.sin(theta), np.cos(theta), 0])

    for m in range(M):
        p_m = np.array([(m - (M - 1) / 2) * d, 0, 0])
        a[m] = np.exp(1j * 2 * np.pi * f / c * u @ p_m)

    return a


d = 0.05
M = 3
theta = 45
f = 1000

print(clc_amv_line(d, M, theta, f))
