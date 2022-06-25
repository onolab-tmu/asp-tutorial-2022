import numpy as np

def set_snr(s, snr):
    A_s = np.linalg.norm(s)
    x = np.random.randn(round(len(s)))
    x = A_s * x /(10**(snr/20)*np.linalg.norm(x))
    return x