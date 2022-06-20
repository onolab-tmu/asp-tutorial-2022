import numpy as np
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


def generate_snr_noise(snr, s1, t2, s2):    # 指定したSN比になるように信号の振幅を調整
    s2 = s2 / np.sqrt(np.sum(s2 ** 2))
    s2 = s2 * np.sqrt(np.sum(s1 ** 2))
    s2 = s2 * 10 ** (-1 * snr / 20)
    return t2, s2


if __name__ == "__main__":
    a = 1.0     # 振幅
    sec = 3.0   # 信号長
    sr = 16000  # サンプリング周波数
    f = 440     # 周波数
    snr = 6     # SN比

    signal = create_signal(a, sec, sr, f)
    noise = create_noise(sec, sr)
    snr_noise = generate_snr_noise(snr, signal[1], *noise)
    mixed_signal = mix_signal(signal[1], *snr_noise)
