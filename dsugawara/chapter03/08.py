import numpy as np


def Frequency_response(a, b, f, sf):

    omega = 2 * np.pi * f / sf
    N = a.size
    M = b.size
    sigma_a = 0j
    sigma_b = 0j

    # a[N]を含むシグマ計算
    for k in range(1, N):
        sigma_a += a[k] * np.e ** (-1j * omega * k)
    # b[M]を含むシグマ計算
    for k in range(0, M):
        sigma_b += b[k] * np.e ** (-1j * omega * k)

    H = sigma_b / (1 + sigma_a)

    return H
