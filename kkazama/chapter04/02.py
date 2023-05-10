import numpy as np

def zero_pad(x, L, S):
    x = np.pad(x, L-S, L-S)
    a = len(x) % S
    if a != 0:
        x = np.pad(x, (0, S-a))
    
    return x

def sep_frame(x, L, S):
    x = zero_pad(x, L, S)
    T = len(x) / S
    xt = np.zeros((T, L))
    for t in range(T):
        for l in range(L):
            xt[t] = x[t * S + l]

    return xt

