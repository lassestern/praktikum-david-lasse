import numpy as np
import matplotlib.pyplot as plt


#Induktivität der Spule
L = 23.954 * 10**(-3)
#Spulenkapazität
C_sp = 0.028 * 10**(-9)
#Kapazität der Kondensatoren
C = 0.7932 * 10**(-9)
#Kopplungskapazität
C_k = np.array([0.997, 2.19, 2.86, 4.74, 6.68, 8.18, 9.99, 12]) * 10**(-9)
#Frequenzverhältnis / Anzahl der Maxima in einer halben Schwebungperiode
n = np.array([0, 3, 4, 7, 9, 11, 13, 16])

#Fehler der Kopplungskapazität
s_C_k = C_k * 0.03

#Frequenz bei gleichphasiger Schwingung (Theorie)
nu_plus_t_element = 1 / (2 * np.pi * np.sqrt(L * (C + C_sp)))
nu_plus_t = np.array([nu_plus_t_element, nu_plus_t_element, nu_plus_t_element, nu_plus_t_element, nu_plus_t_element, nu_plus_t_element, nu_plus_t_element, nu_plus_t_element])

#Schwebungsfrequenz (Theorie)
nu_minus_t = 1 / (2 * np.pi * np.sqrt(L * ((1/C + 2/C_k)**(-1) + C_sp)))

#Fehlerfortpflanzung mit Fehler von C_k
s_nu_minus = (L * C**2) / (2*np.pi*(L*(1/C + 2/C_k)**(-1) + C_sp)**(3/2) * (C_k+2*C)**2) * s_C_k

#Frequenzverhältnis / Anzahl der Maxima in einer halben Schwebungperiode (Theorie)
n_theorie = (nu_minus_t + nu_plus_t) / (2 * (nu_minus_t - nu_plus_t))

#Abweichung des Frequenzverhältnisses vom Theoriewert
a_n = np.abs(n_theorie - n) / n_theorie

#Abweichung der Resonanzfrequenz vom Theoriewert
nu_plus = np.array([35800, 35800, 35800, 35800, 35800, 35800, 35800, 35800])
a_plus = np.abs(nu_plus_t - nu_plus) / nu_plus_t

#Abweichung der Fundamentalfrequenz für gegenphasige Schwingung vom Theoriewert
nu_minus = np.array([56.4, 46.8, 44.6, 41.5, 40.0, 39.4, 38.9, 38.5]) * 10**3
a_minus = np.abs(nu_minus_t - nu_minus) / nu_minus_t

print(s_C_k)
print("Frequenz bei gleichphasiger Schwingung (Theorie):")
print(nu_plus_t)
print("Frequenz bei gegenphasiger Schwingung (Theorie):")
print(nu_minus_t)
print("Fehler der Frequenz bei gegenphasiger Schwingung:")
print(s_nu_minus)
print("Frequenzverhältnis:")
print(n_theorie)
print("Abweichung des Frequenzverhältnisses vom Theoriewert:")
print(a_n)
print("Abweichung der Resonanzfrequenz vom Theoriewert:")
print(a_plus)
print("Abweichung der Fundamentalfrequenz für gegenphasige Schwingung vom Theoriewert:")
print(a_minus)




U_Ampl_plus = np.array([2, 2, 2, 2, 2, 2, 2, 2])
U_Ampl_minus = np.array([0.9, 1, 1, 0.95, 1, 1, 0.95, 0.9])
R = 48
U_1 = 3.6
U_2 = 2.2
x = np.array([0, 1.3 * 10**(-8)])

I_1t = np.array([U_1 / (2*R), U_1 / (2*R)])
I_2t = np.array([U_2 / (2*R), U_2 / (2*R)])
I_1 = U_Ampl_plus / R
I_2 = U_Ampl_minus / R

plt.plot(C_k, I_1, "x", label = r"Strom bei $\nu^+$ Messwerten")
plt.plot(C_k, I_2, "x", label = r"Strom bei $\nu^-$ Messwerten")
plt.plot(x, I_1t, "-", label = r"Strom bei $\nu^+$ Theoriewerten")
plt.plot(x, I_2t, "-", label = r"Strom bei $\nu^-$ Theoriewerten")
plt.xlabel(r"$C_k$ / nF")
plt.ylabel(r"$I$ / A")
plt.legend(loc = "best")
plt.savefig("Stromverlauf.pdf")

plt.clf()


y = np.array([0, 1.3 * 10**(-8)])

plt.plot(C_k, nu_plus, "x", label = r"$\nu^+$ Messwerte")
plt.plot(C_k, nu_minus, "x", label = r"$\nu^-$ Messwerte")
plt.plot(C_k, nu_plus_t, "-", label = r"$\nu^+$ Theoriekurve")
plt.plot(C_k, nu_minus_t, "-", label = r"$\nu^-$ Theoriekurve")
plt.xlabel(r"$C_k$ / nF")
plt.ylabel(r"$\nu$ / kHz")
plt.legend(loc = "best")
plt.savefig("Frequenzverlauf.pdf")
plt.show()









