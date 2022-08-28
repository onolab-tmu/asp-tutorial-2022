import numpy as np


def dft(x):
    N = len(x)
    n = np.arange(N)
    dft_x = np.zeros(N, dtype=complex)
    for k in range(N):
        dft_x[k] = np.sum(x[n] * np.exp(-1j * 2 * np.pi * k * n / N))
    return dft_x


if __name__ == "__main__":
    delta = np.array([1, 0, 0, 0, 0, 0, 0, 0])  # インパルス信号

    dft_delta = dft(delta)
    fft_delta = np.fft.fft(delta)

    print(np.array_equiv(dft_delta, fft_delta))  # 全体が等しいかチェック
    print(np.isclose(dft_delta, fft_delta))  # 要素ごとにおおよそ等しいかチェック
