import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp 
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

#Werte zu den Löchern in Reihenfolge 3 4 5 6 7 in mm
Abstand1_SL, Abstand2_SL = np.genfromtxt("Schiebelehre.txt", unpack=True)
Abstand1_aS, Abstand2_aS = np.genfromtxt("aScan.txt", unpack=True)

#Werte zu den Löcher in Reihenfolge 1 2 in mm
Auflösung1_aS, Auflösung1_SL, Auflösung2_aS, Auflösung2_SL = np.genfromtxt("auflösung.txt", unpack = True)

#Fehlerbehaftete Werte zu den Löchern in Reihenfolge 3 4 5 6 7 in m
Ab1_SL = unp.uarray(Abstand1_SL*10**(-3), 0.00002)
Ab2_SL = unp.uarray(Abstand2_SL*10**(-3), 0.00002)
Ab1_aS = unp.uarray(Abstand1_aS*10**(-3), 0.001)
Ab2_aS = unp.uarray(Abstand2_aS*10**(-3), 0.001)
#Fehlerbehaftete Werte zu den Löchern in Reihenfolge 1 2 in m
Auf1_aS = unp.uarray(Auflösung1_aS*10**(-3), 0.001)
Auf1_SL = unp.uarray(Auflösung1_SL*10**(-3), 0.00002)
Auf2_aS = unp.uarray(Auflösung2_aS*10**(-3), 0.001)
Auf2_SL = unp.uarray(Auflösung2_SL*10**(-3), 0.00002)

#Abweichungen berechnen in %
AbweichungAb1 =  100*(Ab1_aS-Ab1_SL)/Ab1_SL
AbweichungAb2 =  100*(Ab2_aS-Ab2_SL)/Ab2_SL
AbweichungAuf1 = 100*(Auf1_aS-Auf1_SL)/Auf1_SL
AbweichungAuf2 = 100*(Auf2_aS-Auf2_SL)/Auf2_SL

#Theoretische Laufzeiten berechnen

def Laufzeit(c, s):
    return 2*s/c

c_Acryl = 2670

#Laufzeiten in Sekunden
tAb1 = Laufzeit(c_Acryl, Ab1_aS)
tAb2 = Laufzeit(c_Acryl, Ab2_aS)
tAuf1 = Laufzeit(c_Acryl, Auf1_aS)
tAuf2 = Laufzeit(c_Acryl, Auf2_aS)


