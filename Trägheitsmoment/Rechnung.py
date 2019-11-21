import numpy as np

r = 0.2

phi, F = np.genfromtxt('D_Feder.txt', unpack = True)

for c in phi:

    D = F * r / phi

print(D)

D_m = np.sum(D)/len(phi)

print(D_m)