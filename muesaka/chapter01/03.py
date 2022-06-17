import better_exceptions
import soundfile as sf
better_exceptions.MAX_LENGTH = None


if __name__ == "__main__":
    sr = 8000   # サンプリング周波数（変更後）

    data = sf.read('02.wav')[0]  # 信号だけ取り出す
    sf.write('03.wav', data, sr, 'PCM_16')
