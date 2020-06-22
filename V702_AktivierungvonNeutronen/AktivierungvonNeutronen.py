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

def g(x, a, b, c, d):
    return np.log(noms(a) * np.exp(-noms(b)*x) + noms(c) * np.exp(-noms(d)*x))

###########################################################################################################
### Mittelwert der Untergrundzählrate mit Integrationszeit/Messzeit von 300s berechnen
N_U_a = np.array([129, 143, 144, 136, 139, 126, 158])
N_U = ufloat(np.mean(N_U_a), np.std(N_U_a))
N_U_30 = ufloat(np.mean(N_U_a), np.std(N_U_a)) / 10
N_U_15 = ufloat(np.mean(N_U_a), np.std(N_U_a)) / 20
print("Die Untergrundzaehllrate über den Integrationszeitraum 300s, 30s:")
print("{:.3f}".format(N_U))
print("{:.3f}".format(N_U_30))
print("{:.3f}".format(N_U_15))


###########################################################################################################
### Messwerte von Vanadium plotten, fitten und auswerten

# Untergrund von den Messwerten abziehen und Messunsicherheit berechnen
t, N_alt = np.genfromtxt("Vanadium.dat", delimiter = "", unpack = True)
t_besser = t[0:13]
N = unumpy.uarray(N_alt - noms(N_U_30), np.sqrt(N_alt - noms(N_U_30)))
np.savetxt('test.txt', np.column_stack([np.round(noms(N), 2), np.round(stds(N), 2)]), fmt='%10.2f')

# Halblogarithmischen Graphen der korregierten Zählrate N gegen die Zeit t plotten
Z = unumpy.log(N)
Z_besser = Z[0:13]
plt.errorbar(t, noms(Z), xerr = 0, yerr = stds(Z), fmt = "b.", label = r"Messwerte")

# Ausgleichgerade durch alle und durch die erten 14 Messwerte legen
params, cov_matrix = curve_fit(f, t, noms(Z))
m = ufloat(params[0], np.sqrt(cov_matrix[0, 0]))
b = ufloat(params[1], np.sqrt(cov_matrix[1, 1]))

params_besser, cov_matrix_besser = curve_fit(f, t_besser, noms(Z_besser))
m_besser = ufloat(params_besser[0], np.sqrt(cov_matrix_besser[0, 0]))
b_besser = ufloat(params_besser[1], np.sqrt(cov_matrix_besser[1, 1]))

t_lin = np.linspace(t[0], t[-1])
t_lin_besser = np.linspace(30, 440)

plt.plot(t_lin, f(t_lin, *params), "r", label = r"1. Ausgleichsgerade")
plt.plot(t_lin_besser, f(t_lin_besser, *params_besser), "g", label = r"2. Ausgleichsgerade")

plt.xlabel(r"$\Delta t$ [s]")
plt.ylabel(r"$ln{N}$")
plt.legend(loc = "best")
plt.savefig("Bilder/HalbwertszeitGraph.png")
#plt.show()
plt.clf()

# Die Zerfallskonstante und Halbwertszeit berechnen
lam = np.abs(m)
lam_besser = np.abs(m_besser)
T = np.log(2) / lam
T_besser = np.log(2) / lam_besser
N_0_Faktor = exp(b)
N_0_Faktor_besser = exp(b_besser)

# Ergebnisse ausdrucken aus der anfänglichen und verbesserten Rechnung für den Zerfall von Vanadium
print()
print("Parameter der 1. lin. Reg. zum halblogarithmischen Graphen:")
print("{:.6f}".format(m))
print("{:.2f}".format(b))

print()
print("Zerfallskonstante, Halbwertszeit und Abweichung vom theo. Wert für 1. lin. Reg.:")
print("{:.6f}".format(lam))
print("{:.2f}".format(T))
print("{:.5f}".format((224.6 - T) / 224.6))
print("exp(y-Achsenabschnitt) / Vorfaktor für 1. lin. Reg.:")
print("{:.2f}".format(N_0_Faktor))

print()
print("Parameter der 2. verbesserten lin. Reg. zum halblogarithmischen Graphen:")
print("{:.6f}".format(m_besser))
print("{:.2f}".format(b_besser))

print()
print("Zerfallskonstante, Halbwertszeit und Abweichung vom theo. Wert für 2. verbesserte lin. Reg.:")
print("{:.6f}".format(lam_besser))
print("{:.2f}".format(T_besser))
print("{:.5f}".format((224.6 - T_besser) / 224.6))
print("exp(y-Achsenabschnitt) / Vorfaktor für 2. verbesserte lin. Reg.:")
print("{:.2f}".format(N_0_Faktor_besser))


###########################################################################################################
### Messwerte von Rhodium plotten, fitten und auswerten

# Untergrund von den Messwerten abziehen und Messunsicherheit berechnen
t_Rhodium, N_alt_Rhodium = np.genfromtxt("Rhodium.dat", delimiter = "", unpack = True)
t_lang = t_Rhodium[26:44]
N_Rhodium = unumpy.uarray(N_alt_Rhodium - noms(N_U_15), np.sqrt(N_alt_Rhodium - noms(N_U_15)))
np.savetxt('test_lang.txt', np.column_stack([t_Rhodium, np.round(np.log(noms(N_Rhodium)), 4), np.round(stds(unumpy.log(N_Rhodium)), 4)]), fmt='%10.4f')

Z_Rhodium = unumpy.log(N_Rhodium)
Z_lang = Z_Rhodium[26:44]

# Halblogarithmischen Graphen der korregierten Zählrate N_Rhodium gegen die Zeit t_Rhodium plotten
plt.errorbar(t_Rhodium, noms(Z_Rhodium), xerr = 0, yerr = stds(Z_Rhodium), fmt = "b.", label = r"Messwerte")

# Ausgleichgerade durch die letzten 18 Messwerte fitten
params_lang, cov_matrix_lang = curve_fit(f, t_lang, noms(Z_lang))
m_lang = ufloat(params_lang[0], np.sqrt(cov_matrix_lang[0, 0]))
b_lang = ufloat(params_lang[1], np.sqrt(cov_matrix_lang[1, 1]))

# Die Zerfallskonstante und Halbwertszeit für den langlebigen Zerfall berechnen
lam_lang = np.abs(m_lang)
T_lang = np.log(2) / lam_lang
N_0_Faktor_lang = exp(b_lang)

# Untergrund und Zählrate des langlebigen Zerfalls von den Messwerten abziehen
t_kurz = t_Rhodium[0:14]
N_Rhodium_korr = noms(N_Rhodium) - noms(N_0_Faktor_lang) * np.exp(-noms(lam_lang)*noms(t_Rhodium))
np.savetxt('test_kurz.txt', np.column_stack([t_Rhodium, np.round(np.log(np.abs(N_Rhodium_korr)), 4)]), fmt='%10.4f')

Z_kurz = np.log(N_Rhodium_korr[0:14])

# Ausgleichgerade durch die ersten 14 Messwerte fitten
params_kurz, cov_matrix_kurz = curve_fit(f, t_kurz, Z_kurz)
m_kurz = ufloat(params_kurz[0], np.sqrt(cov_matrix_kurz[0, 0]))
b_kurz = ufloat(params_kurz[1], np.sqrt(cov_matrix_kurz[1, 1]))

# Die Zerfallskonstante und Halbwertszeit für den kurzlebigen Zerfall berechnen
lam_kurz = np.abs(m_kurz)
T_kurz = np.log(2) / lam_kurz
N_0_Faktor_kurz = exp(b_kurz)

# Ausgleichsgeraden in den Graphen einzeichnen
t_lin_Rhodium = np.linspace(0, 660)

plt.plot(t_lin_Rhodium, f(t_lin_Rhodium, *params_lang), "r", label = r"Langer Zerfall Ausgleichsgerade")
plt.plot(t_lin_Rhodium, f(t_lin_Rhodium, *params_kurz), "g", label = r"Kurzer Zerfall Ausgleichsgerade")

plt.plot(t_lin_Rhodium, g(t_lin_Rhodium, N_0_Faktor_lang, lam_lang, N_0_Faktor_kurz, lam_kurz), "k", label = r"Errechnete Kurve")
plt.xlabel(r"$\Delta t$ [s]")
plt.ylabel(r"$ln{N}$")
plt.ylim(0)
plt.legend(loc = "best")
plt.savefig("Bilder/HalbwertszeitGraph_Rhodium.png")
plt.show()
plt.clf()


# Messwerte nach Subtraktion von langlebigem Zerfall plotten und die Ausgleichsgerade des kurzlebigen Zerfalls aufzeichnen
t_lin_Rhodium_kurz = np.linspace(0, 230)

plt.plot(t_kurz, noms(Z_kurz), "b.", label = r"Messwerte")
plt.plot(t_lin_Rhodium_kurz, f(t_lin_Rhodium_kurz, *params_kurz), "g", label = r"Kurzer Zerfall Ausgleichsgerade")

plt.xlabel(r"$\Delta t$ [s]")
plt.ylabel(r"$ln{N}$")
plt.legend(loc = "best")
plt.savefig("Bilder/HalbwertszeitGraph_Rhodium_kurzlebig.png")
#plt.show()
plt.clf()


# Ergebnisse ausdrucken für den langlebigen und kurzlebigen Zerfall von Rhodium
print()
print("Parameter der lin. Reg. zum halblogarithmischen Graphen zum langlebigen Zerfall:")
print("{:.6f}".format(m_lang))
print("{:.2f}".format(b_lang))

print()
print("Zerfallskonstante, Halbwertszeit und Abweichung vom theo. Wert für lin. Reg. des langlebigen Zerfalls:")
print("{:.6f}".format(lam_lang))
print("{:.1f}".format(T_lang))
print("{:.3f}".format((260.4 - T_lang) / 260.4))
print("exp(y-Achsenabschnitt) / Vorfaktor für lin. Reg. des langlebigen Zerfalls:")
print("{:.2f}".format(N_0_Faktor_lang))

print()
print("Parameter der lin. Reg. zum halblogarithmischen Graphen zum kurzlebigen Zerfall:")
print("{:.6f}".format(m_kurz))
print("{:.2f}".format(b_kurz))

print()
print("Zerfallskonstante, Halbwertszeit und Abweichung vom theo. Wert für lin. Reg. des kurzlebigen Zerfalls:")
print("{:.6f}".format(lam_kurz))
print("{:.1f}".format(T_kurz))
print("{:.3f}".format((42.3 - T_kurz) / 42.3))
print("exp(y-Achsenabschnitt) / Vorfaktor für lin. Reg. des kurzlebigen Zerfalls:")
print("{:.2f}".format(N_0_Faktor_kurz))




























































