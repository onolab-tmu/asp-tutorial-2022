import numpy as np

def zero_pad(x, L, S):
    x = np.pad(x, L-S, L-S)
    a = len(x) % S
    if a != 0:
        x = np.pad(x, (0, S-a))
    
    return x
