import soundfile as sf
from scipy.signal import decimate

if __name__ == "__main__":
    s = 3
    fs_re = 8000
    x, sr = sf.read("sound_noize.wav")
    x_re = decimate(x, 2)

    sf.write("sound_re.wav", data=x_re, samplerate=fs_re, subtype="PCM_16")
