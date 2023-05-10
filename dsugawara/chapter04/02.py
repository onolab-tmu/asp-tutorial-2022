import numpy as np


def padding(L, S, x):

    x = np.pad(x, [L - S, L - S])
    temp = S - (x.size % S)  # 末尾に詰める0の個数を求める
    x = np.pad(x, [0, temp])
    return x


def frame_cut(L, S, x):
    N = x.size
    T = ((N - L) // S) + 1  # フレーム数．後で確認
    x_cut = np.empty([T, L])  # 出力
    x_pad = padding(L, S, x)
    for t in range(0, T):
        x_cut[t] = x_pad[t * S : t * S + L]
    return x_cut
