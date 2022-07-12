import numpy as np


# 関数
def syn_wnd(w, S):
    """合成窓を生成する

    Args:
        w (ndarray): 窓関数
        S (int): シフト幅

    Returns:
        ws (ndarray): 合成窓（float型1次元配列）

    """
    L = len(w)
    Q = L//S
    ws = np.zeros(L)

    for l in range(L):
        tmp = 0
        for m in range(-Q+1,Q):
            if l-m*S < L:
                tmp += w[l-m*S] ** 2
        ws[l] = w[l] / tmp

    return ws