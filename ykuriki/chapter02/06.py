import numpy as np
import matplotlib.pyplot as plt


fs = 16000
f = 440
r = 1
sec = 3

t = np.arange(0, fs * sec) / fs
sig = r * np.sin(f * 2 * np.pi * t)

fft_sig = np.fft.fft(sig)

amp = 20 * np.log10(np.abs(fft_sig))
phase = 20 * np.log10(np.angle(fft_sig))

freq = np.arange(len(fft_sig)) / len(fft_sig) * fs


# プロット
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 5))

p0 = ax[0].plot(freq, amp)
ax[0].set_xlabel("frequency [Hz]")
ax[0].set_ylabel("amplitude spectrum [dB]")
ax[0].set_title("Amplitude spectrum")
ax[0].grid()

p0 = ax[1].plot(freq, phase)
ax[1].set_xlabel("frequency [Hz]")
ax[1].set_ylabel("phase spectrum [dB]")
ax[1].set_title("Phase spectrum")
ax[1].grid()

plt.tight_layout()

plt.show()
