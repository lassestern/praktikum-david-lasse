

import numpy as np
s = 0
i=0
z=0

x, F = np.genfromtxt('werte.txt', unpack=True)

for c in x:
    D=F/x
    
    
print(np.sum(D)/len(x))



