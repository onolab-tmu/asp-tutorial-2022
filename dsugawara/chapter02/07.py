import numpy as np


# Humming窓
def Humming(N):
    w = []
    for n in range(N):
        a = 0.54 - 0.46 * np.cos(2*np.pi*n/(N-1))
        w.append(a)
    return w
