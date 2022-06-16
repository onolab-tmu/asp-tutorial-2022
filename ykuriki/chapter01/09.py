import numpy as np
import wave


# 音声データの読み取り
wavfile = "./08.wav"
wav = wave.open(wavfile, "rb")
ch = wav.getnchannels()
wid = wav.getsampwidth()
sfrq = wav.getframerate()
siglen = wav.getnframes()
sig = wav.readframes(siglen)
sig = np.frombuffer(sig, dtype=np.int16)
sig = sig / np.iinfo(np.int16).max
wav.close()


# パラメータ
fs = 8000

# 音声ファイル出力
output = (sig[::2] * np.iinfo(np.int16).max).astype(np.int16)
wav = wave.open("./09.wav", "wb")
wav.setnchannels(ch)
wav.setsampwidth(wid)
wav.setframerate(fs)
wav.writeframes(output)
wav.close()
