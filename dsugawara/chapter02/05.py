import numpy as np
import matplotlib.pyplot as plt


# impulse
delta = np.zeros(8)
delta[0] = 1

dft_delta = np.fft.fft(delta)

# スペクトルを求める
amp = np.abs(dft_delta)
angle = np.angle(dft_delta)

# plot
fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax1.stem(amp)
ax2.stem(angle)
ax1.set_title("amplitude")
ax2.set_title("angle")
fig.tight_layout()
plt.savefig("05py_spectrum.png")
