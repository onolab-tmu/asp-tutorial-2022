import numpy as np
import better_exceptions
import soundfile as sf
better_exceptions.MAX_LENGTH = None


def create_signal(a, sec, sr, f):   # 信号生成
    t = np.linspace(0, sec, int(sr * sec))
    s = a * np.sin(2 * np.pi * f * t)
    return t, s


if __name__ == "__main__":
    a = 1.0     # 振幅
    sec = 3.0   # 信号長
    sr = 16000  # サンプリング周波数
    f = 440     # 周波数

    signal = create_signal(a, sec, sr, f)
    sf.write('02.wav', signal[1], sr, 'PCM_16')
