import numpy as np

def hamming(N):
    w = 0.54 - 0.46 * np.cos(2* np.pi* np.arange(N)/ (N-1))
    return w