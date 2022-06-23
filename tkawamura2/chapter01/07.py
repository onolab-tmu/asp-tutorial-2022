import numpy as np
import math

def snr(s, x):
    N = len(s)
    if N == len(x):
        return np.NaN
    sn_ratio = np.linalg.norm(s)**2/np.linalg.norm(x)**2
    return 10*math.log(sn_ratio)