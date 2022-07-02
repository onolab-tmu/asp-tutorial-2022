import numpy as np
import matplotlib.pyplot as plt


def frequency_response(a, b, f, fs):
    """
    周波数応答を計算する
    Input:
         a : coefficient of y
        b : coefficient of x
        f: 周波数
        fs: サンプリング周波数
    Output:
        H: 周波数応答
    """
    N = a.size
    M = b.size
    omega = 2 + np.pi * f / fs
    # a についての処理
    sum_a = np.sum(a * np.exp(-1j * omega * np.arange(1, N)))
    # b についての処理
    sum_b = np.sum(b * np.exp(-1j * omega * np.arange(0, M)))
    H = sum_b / (1 + sum_a)

    return H


if __name__ == "__main__":

    fs = 16000
    a = np.array([1, 0.3])
    b = np.array([0.4])
    N = 10
    H = np.zeros(N, dtype="complex")
    for i in range(N):
        f = (i / N) * fs
        H[i] = frequency_response(a, b, f, fs)
        print(f, H)

    # 振幅特性のプロット
    plt.subplot(2, 1, 1)
    plt.stem(np.abs(H))
    plt.grid()
    plt.title("Amplitude")
    # 位相特性のプロット
    plt.subplot(2, 1, 2)
    plt.stem(np.angle(H))
    plt.grid()
    plt.title("Angle")
    plt.tight_layout()
    plt.show()
