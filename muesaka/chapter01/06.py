import numpy as np
import matplotlib.pyplot as plt
import better_exceptions
better_exceptions.MAX_LENGTH = None


def create_signal(a, sec, sr, f):   # 信号生成
    t = np.linspace(0, sec, int(sr * sec))
    s = a * np.sin(2 * np.pi * f * t)
    return t, s


def create_noise(sec, sr):  # 白色雑音生成
    t = np.linspace(0, sec, int(sr*sec))
    s = np.random.random(len(t))
    return t, s


def mix_signal(s1, t2, s2):  # 混合信号合成
    s = np.array(s1) + np.array(s2)
    return t2, s


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
    f = 440     # 周波数
    plot_right = 0.03   # x軸プロット上限

    signal = create_signal(a, sec, sr, f)
    noise = create_noise(sec, sr)
    mixed_signal = mix_signal(signal[1], *noise)
    plot_signal(*mixed_signal, plot_right, '05.pdf')
