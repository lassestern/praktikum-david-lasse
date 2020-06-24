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
    return a * x + b

#######################################################################################################################################################
### Wurzel des Photostroms gegen angelegte Spannung auftragen, Ausgleichgerade über lin. Abschnitt der Kurve machen und damit die Nullstelle berechnen
# Für gelbes Licht lin. Reg. mit den letzten 5 Messwerten
U_gelb, I_gelb, I_gelb_u = np.genfromtxt("gelbesLicht.txt", delimiter = "", unpack = True)

plt.errorbar(U_gelb, np.sqrt(I_gelb), xerr = 0, yerr = np.sqrt(I_gelb_u), fmt = "b.", label = r"Messwerte")

params_gelb, cov_matrix_gelb = curve_fit(f, U_gelb[30:35], np.sqrt(I_gelb[30:35]))

U_gelb_lin = np.linspace(-2, 0.4)

plt.plot(U_gelb_lin, f(U_gelb_lin, *params_gelb), "r", label = r"Ausgleichsgerade")
plt.axhline(0, color = "g", linestyle = "--")

plt.xlabel(r"$U$ [V]")
plt.ylabel(r"$\sqrt{I}$ $[\sqrt{nA}]$")
plt.legend(loc = "best")
plt.savefig("Bilder/Photostrom_Spannung_gelb.png")
#plt.show()
plt.clf()

m_gelb = ufloat(params_gelb[0] , np.sqrt(cov_matrix_gelb[0, 0]))
b_gelb = ufloat(params_gelb[1] , np.sqrt(cov_matrix_gelb[1, 1]))

U_G_gelb = -b_gelb/m_gelb

print("Steigung in [sqrt(A)/V] und y-Achsenabschnitt der lin. Reg. für gelbes Licht:")
print(m_gelb * np.sqrt(10**(-9)))
print(b_gelb)
print("Nullstelle / U_G für gelbes Licht:")
print(U_G_gelb)

# Für gruenes Licht lin. Reg. mit den letzten 5 Messwerten
U_gruen, I_gruen, I_gruen_u = np.genfromtxt("gruenesLicht.txt", delimiter = "", unpack = True)

plt.errorbar(U_gruen, np.sqrt(I_gruen), xerr = 0, yerr = np.sqrt(I_gruen_u), fmt = "b.", label = r"Messwerte")

params_gruen, cov_matrix_gruen = curve_fit(f, U_gruen[11:16], np.sqrt(I_gruen[11:16]))

U_gruen_lin = np.linspace(-1, 0.55)

plt.plot(U_gruen_lin, f(U_gruen_lin, *params_gruen), "r", label = r"Ausgleichsgerade")
plt.axhline(0, color = "g", linestyle = "--")

plt.xlabel(r"$U$ [V]")
plt.ylabel(r"$\sqrt{I}$ $[\sqrt{nA}]$")
plt.legend(loc = "best")
plt.savefig("Bilder/Photostrom_Spannung_gruen.png")
#plt.show()
plt.clf()

m_gruen = ufloat(params_gruen[0] , np.sqrt(cov_matrix_gruen[0, 0]))
b_gruen = ufloat(params_gruen[1] , np.sqrt(cov_matrix_gruen[1, 1]))

U_G_gruen = -b_gruen/m_gruen

print()
print("Steigung in [sqrt(A)/V] und y-Achsenabschnitt der lin. Reg. für gruenes Licht:")
print(m_gruen * np.sqrt(10**(-9)))
print(b_gruen)
print("Nullstelle / U_G für gruenes Licht:")
print(U_G_gruen)

# Für violettes Licht lin. Reg. mit den letzten 9 Messwerten
U_violett, I_violett, I_violett_u = np.genfromtxt("violettesLicht.txt", delimiter = "", unpack = True)

plt.errorbar(U_violett, np.sqrt(I_violett), xerr = 0, yerr = np.sqrt(I_violett_u), fmt = "b.", label = r"Messwerte")

params_violett, cov_matrix_violett = curve_fit(f, U_violett[3:12], np.sqrt(I_violett[3:12]))

U_violett_lin = np.linspace(0, 1.1)

plt.plot(U_violett_lin, f(U_violett_lin, *params_violett), "r", label = r"Ausgleichsgerade")
plt.axhline(0, color = "g", linestyle = "--")

plt.xlabel(r"$U$ [V]")
plt.ylabel(r"$\sqrt{I}$ $[\sqrt{nA}]$")
plt.legend(loc = "best")
plt.savefig("Bilder/Photostrom_Spannung_violett.png")
#plt.show()
plt.clf()

m_violett = ufloat(params_violett[0] , np.sqrt(cov_matrix_violett[0, 0]))
b_violett = ufloat(params_violett[1] , np.sqrt(cov_matrix_violett[1, 1]))

U_G_violett = -b_violett/m_violett

print()
print("Steigung in [sqrt(A)/V] und y-Achsenabschnitt der lin. Reg. für violettes Licht:")
print(m_violett * np.sqrt(10**(-9)))
print(b_violett)
print("Nullstelle / U_G für violettes Licht:")
print(U_G_violett)


#######################################################################################################################################################
###Gegenspannung gegen die Frequenz des Lichtes auftragen und mit lin. Reg. die Austrittsarbeit und die Steigung berechnen
frequenz = const.c / (np.array([434, 546, 578]) * 10**(-9))
U_G = np.array([U_G_violett, U_G_gruen, U_G_gelb])
print()
print("Frequenzen des violetten, gruenen und gelben Lichtes in THz:")
for x in np.nditer(frequenz * 10**(-12)):
    print("{:.0f}".format(x))

plt.errorbar(frequenz * 10**(-12), noms(U_G), xerr = 0, yerr = stds(U_G), fmt = "b.", label = r"Messwerte")

params, cov_matrix = curve_fit(f, frequenz * 10**(-12), noms(U_G))

frequenz_lin = np.linspace(500, 700)

plt.plot(frequenz_lin, f(frequenz_lin, *params), "r", label = r"Ausgleichsgerade")

plt.xlabel(r"$\nu$ [THz]")
plt.ylabel(r"$U_G$ [V]")
plt.legend(loc = "best")
plt.savefig("Bilder/Spannung_Frequenz.png")
#plt.show()
plt.clf()

m = ufloat(params[0] , np.sqrt(cov_matrix[0, 0]))
b = ufloat(params[1] , np.sqrt(cov_matrix[1, 1]))
h_eV = const.h / const.e

print(h_eV)
print("Steigung der lin. Reg. / (h durch e) und die Abweichung zum theo. Wert von h in eV:")
print(m * 10**(-12))
print((m*10**(-12) - h_eV) / h_eV)
print("y-Achsenabschnitt, daraus die Austrittsarbeit der Kathode in eV und die Abweichung zum theo. Wert von Caesium:")
print(b)
print(-b)
print((2.14 + b) / 2.14)


#######################################################################################################################################################
### Den Photostrom gegen angelegte Spannung auftragen und versuchen Kurve zu erklären
plt.errorbar(U_gelb, I_gelb, xerr = 0, yerr = I_gelb_u, fmt = "b.", label = r"Messwerte")
plt.xlabel(r"$U$ [V]")
plt.ylabel(r"$I$ $[nA]$")
plt.legend(loc = "best")
plt.savefig("Bilder/Photostrom_gelb.png")
#plt.show()
plt.clf()



#np.savetxt('test_gelb.txt', np.column_stack([U_gelb, I_gelb, I_gelb_u, np.sqrt(I_gelb)]), fmt='%10.2f')
#np.savetxt('test_gruen.txt', np.column_stack([U_gruen, I_gruen, I_gruen_u, np.sqrt(I_gruen)]), fmt='%10.2f')
#np.savetxt('test_violett.txt', np.column_stack([U_violett, I_violett, I_violett_u, np.sqrt(I_violett)]), fmt='%10.2f')

































