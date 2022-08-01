import numpy as np
import matplotlib.pyplot as plt


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
    a = np.empty([u.T.shape[0], p.shape[1]], dtype="complex")  # 　a[1, M]になるはず
    a = np.exp(2j * np.pi * f / c * np.dot(u.T, p))

    return a


def plot_beampattern(w, p, fs):

    """ビームパターンを描画

    Args:
        w (ndarray): 周波数領域におけるビームフォーマのフィルタ（2次元配列）
        p (ndarray): マイクアレイの座標（2次元配列）
        fs (int): サンプリング周波数

    Return:
        png file: ビームパターンの描画

    """
    F = w.shape[0]
    M = p.shape[1]
    a = np.empty([M, F, 360], dtype="complex")
    psi = np.empty([F, 360], dtype="complex")
    for theta in range(0, 360):
        for f in range(0, F):
            a[:, f, theta] = array_vector(p, theta, (fs / 2) / (F - 1) * f)
            psi[:, theta] = np.dot(np.conjugate(w[f, :].T), a[:, f, theta])

    plt.pcolormesh(np.arange(0, 360), np.arange(F), 20 * np.log10(np.abs(psi)))
    plt.colorbar()
    plt.savefig("08py_beampattern.png")


# main
L = 1024  # 窓幅
S = 512  # シフト幅
F = L // 2 + 1  # 周波数ビンの総数
fs = 16000
d = 0.05
p = np.array([[-d, 0, 0], [0, 0, 0], [d, 0, 0]])  # マイクアレイの座標

tau = np.array([0, 10 / fs, 20 / fs])
w = np.empty([F, 3], dtype="complex")
for Fn in range(0, F):
    f = (fs / 2) / (F - 1) * Fn
    w[Fn, :] = 1 / 3 * np.exp(-2j * np.pi * f * tau)

plot_beampattern(w, p, fs)
