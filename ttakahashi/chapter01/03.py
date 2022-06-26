import soundfile as sf

y, sr = sf.read("outputs/02.wav")
sf.write("outputs/03.wav", y, 8000, format="WAV", subtype="PCM_16")

print("success!")
