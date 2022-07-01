import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    A = 1
    f = 440.0
    sec = 3.0
    fs = 16000

    t = np.arange(0, sec * fs) / fs
    y = A * np.sin(2 * np.pi * f * t)

    y_npfft = np.fft.fft(y)

    y_amp = 20 * np.log10(np.abs(y_npfft))
    y_angle = 20 * np.log10(np.angle(y_npfft))

    fig = plt.figure()
    fig_amp = fig.add_subplot(2, 1, 1)
    fig_angle = fig.add_subplot(2, 1, 2)
    fig_amp.plot(y_amp)
    fig_angle.plot(y_angle)
    fig_amp.set_title("Amplitude")
    fig_angle.set_title("Angle")
    fig.tight_layout()
    plt.show()
