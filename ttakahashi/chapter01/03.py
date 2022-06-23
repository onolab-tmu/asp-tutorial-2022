####################################################################
##### @ref https://www.wizard-notes.com/entry/python/soundfile #####
##### @author Tomohiro Takahashi 2022/06/14                    #####
####################################################################

import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

y, sr = sf.read('output/02.wav')
sf.write('output/03.wav', y, 8000, format='WAV', subtype='PCM_16')

print('success!')