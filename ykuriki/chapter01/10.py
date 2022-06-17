import numpy as np
import wave
import matplotlib.pyplot as plt


# パラメータ
tap = 5

filter = np.ones(tap) / tap

# 音声データの読み取り
wavfile = "./09.wav"
wav = wave.open(wavfile, "rb")
sfrq = wav.getframerate()
siglen = wav.getnframes()
sig = wav.readframes(siglen)
sig = np.frombuffer(sig, dtype=np.int16)
sig = sig / np.iinfo(np.int16).max
wav.close()

t_sig = np.arange(0, siglen) / sfrq

cnv = np.convolve(sig, filter)
t_cnv = np.arange(0, len(cnv)) / sfrq


# プロット
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 5))

p0 = ax[0].plot(t_sig, sig)
ax[0].set_xlim([0, 0.03])
ax[0].set_ylim([-1.1, 1.1])
ax[0].set_xlabel("time [s]")
ax[0].set_ylabel("amplitude")
ax[0].set_title("original")
ax[0].grid()

p0 = ax[1].plot(t_cnv, cnv)
ax[1].set_xlim([0, 0.03])
ax[1].set_ylim([-1.1, 1.1])
ax[1].set_xlabel("time [s]")
ax[1].set_ylabel("amplitude")
ax[1].set_title("convolution")
ax[1].grid()

plt.tight_layout()

plt.show()
