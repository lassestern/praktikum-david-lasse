import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from scipy.optimize import curve_fit
import scipy.constants as const

def f(x, a, b):
    return a*x + b

def g(x, c, d):
    return c*x + d

###########################################################################################################
#Mittelwert der Untergrundzählrate mit Integrationszeit/Messzeit von 300s berechnen
N_U_a = np.array([129, 143, 144, 136, 139, 126, 158])
N_U = ufloat(np.mean(N_U_a), np.std(N_U_a))
print("Die Untergrundzaehllrate über den Integrationszeitraum 300s, 30:")
print("{:.3f}".format(N_U))
print("{:.3f}".format(N_U / 10))


###########################################################################################################
#Untergrund von den Messwerten abziehen und Messunsicherheit berechnen
t, N_alt = np.genfromtxt("Vanadium.dat", delimiter = "", unpack = True)
t_1 = t[0:13]
N = unumpy.uarray(N_alt - noms(N_U) / 10, np.sqrt(N_alt - noms(N_U) / 10))
np.savetxt('test.txt', np.column_stack([np.round(noms(N), 2), np.round(stds(N), 2)]), fmt='%10.2f')

#Halblogarithmischen Graphen der korregierten Zählrate N gegen die Zeit t plotten
Z = unumpy.log(N)
Z_1 = Z[0:13]
plt.errorbar(t, noms(Z), xerr = 0, yerr = stds(Z), fmt = "b.", label = r"Messwerte")

#Ausgleichgerade durch alle Messwerte legen
params, cov_matrix = curve_fit(f, t, noms(Z))
params_1, cov_matrix_1 = curve_fit(g, t_1, noms(Z_1))
t_lin = np.linspace(t[0], t[-1])
t_lin_1 = np.linspace(30, 440)

plt.plot(t_lin, f(t_lin, *params), "r", label = r"1. Ausgleichsgerade")
plt.plot(t_lin_1, g(t_lin_1, *params_1), "g", label = r"2. Ausgleichsgerade")

plt.xlabel(r"$\Delta t$ [s]")
plt.ylabel(r"$ln{N}$")
plt.legend(loc = "best")
plt.savefig("Bilder/HalbwertszeitGraph.png")
#plt.show()
plt.clf()

#Die Zerfallskonstante und Halbwertszeit berechnen
lam = np.abs(params[0])
lam_1 = np.abs(params_1[0])
T = np.log(2) / lam
T_1 = np.log(2) / lam_1
N_0 = np.exp(params[1])
N_0_1 = np.exp(params_1[1])

print("Zerfallskonstante, Halbwertszeit und Abweichung vom theo. Wert für 1. und 2. lin. Reg.:")
print(lam)
print(lam_1)
print(T)
print(T_1)
print((224.6 - T) / T)
print((224.6 - T_1) / T_1)
print("exp(y-Achsenabschnitt) / Vorfaktor:")
print(N_0)
print(N_0_1)





































































