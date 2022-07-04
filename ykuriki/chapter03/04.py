import numpy as np
import matplotlib.pyplot as plt


# 関数
def line_conv(x, h):
    """線形たたみこみを行う

    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）

    Returns:
        y (ndarray): 畳み込みの実行結果（1次元配列）

    """
    x_size = len(x)
    h_size = len(h)
    y_size = x_size + h_size - 1

    y = np.zeros(y_size)

    # 纏めて計算
    for i in range(x_size):
        y[i : i + h_size] += x[i] * h

    return y


def circul_conv(x, h):
    """x[n]とh[n]の巡回たたみこみを計算する（周期的）

    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）

    Returns:
        y (ndarray): 畳み込み結果（1次元配列）

    """
    X = np.fft.fft(x)
    H = np.fft.fft(h)
    y = np.fft.ifft(X * H)

    return y


def circul_conv_pad(x, h):
    """x[n]とh[n]の巡回たたみこみを計算する（非周期的）

    Args:
        x (ndarray): 信号（1次元配列）
        h (ndarray): インパルス応答（1次元配列）

    Returns:
        y (ndarray): 畳み込み結果（1次元配列）

    """
    x_size = len(x)
    h_size = len(h)

    X = np.fft.fft(np.block([x, np.zeros(h_size)]))
    H = np.fft.fft(np.block([h, np.zeros(x_size)]))
    y = np.fft.ifft(X * H)

    return y[:-1]


x = np.array([4, 3, 2, 1])
h = np.array([1, 0, -1, 0])

y_line = line_conv(x, h)
y_circul = circul_conv(x, h)
y_circul_pad = circul_conv_pad(x, h)

# プロット
fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(6, 7))

p0 = ax[0].stem(np.arange(len(y_line)), y_line)
ax[0].set_xlabel("n")
ax[0].set_ylabel("amplitude")
ax[0].set_ylim([-4.5, 4.5])
ax[0].set_title("Linear convolution")
ax[0].grid()

p1 = ax[1].stem(np.arange(len(y_circul)), y_circul.real)
ax[1].set_xlabel("n")
ax[1].set_ylabel("amplitude")
ax[1].set_ylim([-4.5, 4.5])
ax[1].set_title("Circular convolution")
ax[1].grid()

p2 = ax[2].stem(np.arange(len(y_circul_pad)), y_circul_pad.real)
ax[2].set_xlabel("n")
ax[2].set_ylabel("amplitude")
ax[2].set_ylim([-4.5, 4.5])
ax[2].set_title("Circular convolution (Zero pad)")
ax[2].grid()

plt.tight_layout()

plt.show()
