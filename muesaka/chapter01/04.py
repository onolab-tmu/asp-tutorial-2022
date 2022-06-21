import numpy as np
import better_exceptions
import soundfile as sf
better_exceptions.MAX_LENGTH = None


def create_signal(a, sec, sr, f):   # 信号生成
    t = np.linspace(0, sec, int(sr * sec))
    s = a * np.sin(2 * np.pi * f * t)
    return t, s


def generate_stereo_signal(s1, s2):     # ステレオ信号合成
    return [[s1[i], s2[i]] for i in range(len(s1))]


if __name__ == "__main__":
    a = 1.0     # 振幅
    sec = 3.0   # 信号長
    sr = 16000  # サンプリング周波数
    f1 = 440    # 周波数1（440 Hz）
    f2 = 660    # 周波数2（660 Hz）

    s1 = create_signal(a, sec, sr, f1)
    s2 = create_signal(a, sec, sr, f2)
    s3 = generate_stereo_signal(s1[1], s2[1])
    sf.write('04.wav', s3[1], sr, 'PCM_16')
