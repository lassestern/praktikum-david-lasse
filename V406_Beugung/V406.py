import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.optimize import curve_fit
import scipy.constants as const

# Griechische Buchstaben
#greek_letterz=[chr(code) for code in range(945,970)]
#print(greek_letterz)


def f(x, A, b):
    return A**2 * (np.sinc(b * x))**2


###########################################################################################################################################
### Einzelspalt-Messwerte plotten und die theoretische Kurve fitten
#dunkelstrom ist 1 nA, also kleiner als Messunsucherheit beim Ablesen des Stromes bei den Messerten
x, I, I_fehler = np.genfromtxt("Intensitaetsverteilung.txt", delimiter = "", unpack = True)
d = 1162
lam = 633 * 10**(-9)

#xx = x / (np.sqrt(x**2 + d**2))
#print(xx)

phi_rad = np.arctan(x / d)
phi = phi_rad * 180/np.pi
sin_phi = np.sin(phi_rad)

#print(phi_rad)
I = unumpy.uarray([I, I_fehler])

params, cov_matrix = curve_fit(f, sin_phi, noms(I))
a = ufloat(params[0], np.sqrt(cov_matrix[0, 0]))
b = ufloat(params[1], np.sqrt(cov_matrix[1, 1]))
phi_lin = np.linspace(phi[0], phi[-1], 200)
sin_phi_lin = np.sin(phi_lin * np.pi/180)
print("{:.2f}".format(a))
print("{:.2f}".format(b))
print(b * lam)

print((noms(b*lam) - 0.00015) / 0.00015)

plt.errorbar(phi, noms(I), xerr = 0, yerr = stds(I), fmt = "b.", label = r"Messwerte")
plt.plot(phi_lin, f(sin_phi_lin, *params), "r", label = r"Theoretische Kurve")

plt.xlabel(r"$\varphi$ [°]")
plt.ylabel(r"$I$ [$\mu$A]")
plt.legend(loc="best")
plt.savefig("Bilder/Einzelspalt_Messwerte.png")
#plt.show()
plt.clf()



np.savetxt('test.txt', np.column_stack([x, phi, noms(I), stds(I)]), fmt='%10.2f')
















































































