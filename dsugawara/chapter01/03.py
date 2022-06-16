 #2.で保存した wav ファイルを読み込み，サンプリング周波数を 8kHz に変換して保存せよ．

from os import lseek
import soundfile
file = "02py_sin.wav"
data, samplerate = soundfile.read(file)


soundfile.write(file="03py_sin.wav", data=data, samplerate=8000)