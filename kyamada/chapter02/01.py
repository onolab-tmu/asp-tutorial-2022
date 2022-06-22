import numpy as np


def dft(x):
    """
    DFT
    Input:
        x: input array
    Output:
        X: output DFT array
    """
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp((-2j * np.pi * k * n) / N)

        # X = np.sum(x * np.exp((-2j * np.pi * k * np.arange(N)) / N))
    return X


def idft(x):
    """
    IDFT
    Input:
        x: input array
    Output:
        X: output DFT array
    """
    N = len(x)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += x[n] * np.exp((2j * np.pi * k * n) / N) / N
    return X


if __name__ == '__main__':
    x = np.array([1, 0, 0, 0, 0, 0, 0, 0])
    X = dft(x)
    X_fft = np.fft.fft(x)
    print(X)
    print(X_fft)
    y = idft(X)
