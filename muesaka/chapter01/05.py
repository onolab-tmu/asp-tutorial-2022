import numpy as np
import matplotlib.pyplot as plt
import better_exceptions
better_exceptions.MAX_LENGTH = None


def create_noise(sec, sr):  # 白色雑音生成
    t = np.linspace(0, sec, int(sr*sec))
    s = np.random.random(len(t))
    return t, s


def plot_signal(t, s, right, filename):  # 単一信号プロット
    plt.plot(t, s)
    plt.xlim(0, right)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.savefig(filename)
    plt.show()


if __name__ == "__main__":
    a = 1.0     # 振幅
    sec = 3.0   # 信号長
    sr = 16000  # サンプリング周波数
    plot_right = 0.03   # x軸プロット上限

    noise = create_noise(sec, sr)
    plot_signal(*noise, plot_right, '05.pdf')
