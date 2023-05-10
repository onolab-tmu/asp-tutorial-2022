# SN比を指定した信号の混合（確認）: 8.で実装した関数を用いて，6.と同様にホワイトノイズと正弦波の混合信号を作成しwavファイルとして保存せよ．ただし，SN比が6dBとなるようにすること．


import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf


def main():
    filename = "mixture.wav"
    filename_down = "mixture_down.wav"
    fs_down = 8000  # (Hz)

    mixture, fs = sf.read(filename)  # 書き出したファイルの読み込み
    print(f"sampling rage: {fs} (Hz)")

    step_down = int(fs // fs_down)  # 2 (sample)
    mixture_down = mixture[::step_down]  # 単純に間引く (整数倍だとうまくいく)

    # save
    sf.write(filename_down, mixture_down, fs_down, subtype="FLOAT")  # PCMでないことに注意

    # 確認方法 (プロットしてみる，1サンプルおきに点が重なる)
    # mixture_down2, fs_down2 = sf.read(filename_down)  # 書き出したファイルの読み込み

    # sig_len_sample = len(mixture)  # signal length
    # sig_len_sample_down2 = len(mixture_down2)

    # t = np.arange(sig_len_sample) / fs  # time
    # t_down2 = np.arange(sig_len_sample_down2) / fs_down2

    # # plot
    # plt.title("Downsample")
    # plt.plot(t, mixture, marker=".", label="Raw")
    # plt.plot(t_down2, mixture_down2, marker="o", label="Downsampled")
    # plt.xlim(0, 10 / fs)
    # plt.legend()
    # plt.show()


if __name__ == "__main__":
    main()
