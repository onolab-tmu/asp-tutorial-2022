import numpy as np
import matplotlib.pyplot as plt


# 関数
def clc_amv(p, theta, f):
    """アレイマニフォールドベクトルを計算する

    Args:
        p: アレイの座標
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


def plt_bmpt(w, p, fs):
    """ビームパターンを描画する

    Args:
        w (ndarray): ビームフォーマ
        p (ndarray): マイクアレイの座標
        fs (int): サンプリング周波数

    """
    F = len(w)

    deg = np.arange(361)
    fq = np.arange(F) * (fs / 2) / (F - 1)
    psi = np.zeros((F, 361), dtype="complex")

    for f in range(F):
        for theta in range(361):
            a_f = clc_amv(p, theta, fq[f])
            psi[f, theta] = np.conjugate(w[f]) @ a_f

    plt.pcolormesh(deg, fq, 20 * np.log10(abs(psi)))
    plt.xlabel("phase [deg]")
    plt.ylabel("amplitude")
    plt.colorbar()
    plt.tight_layout()
    plt.show()

    return


D = np.array([0.02, 0.05, 0.1])
M = 3
theta = 45
fs = 16000
F = 513
c = 334


for d in D:
    p = np.vstack([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])
    w = np.zeros((F, M), dtype="complex")
    for f in range(F):
        fq = f * (fs / 2) / (F - 1)
        w[f] = np.exp(1j * 2 * np.pi * fq / c) / M

    plt_bmpt(w, p, fs)
