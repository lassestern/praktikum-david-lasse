

import numpy as np


x, F = np.genfromtxt('werte.txt', unpack=True)

for c in x:
    D=F/x
    
M = np.sum(D)/len(x)

for k in D:
    s = (D - M)**2

sx = np.sqrt((1/9) * np.sum(s))
    
print(M)
print(s)
print(sx)
print(sx/np.sqrt(10))




