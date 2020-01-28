import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat
from scipy.optimize import curve_fit


#Induktivität der Spule
L = 10.11 * 10**(-3)
s_L = 0.03 * 10**(-3)
#Kapazität des Kondensators
C = 2.093 * 10**(-9)
s_C = 0.003 * 10**(-9)
#Widerstand
R = 48.1
s_R = 0.1

#Zeit von Anfang der Schwingung, Amplitude der Kondensatorspannung
t, U_ampl = np.genfromtxt("einhuellende.txt", delimiter = ",", unpack = True)
t_pos, U_ampl_pos = np.genfromtxt("einhuellende_pos.txt", delimiter = ",", unpack = True)


U_0 = 145
mu = R / (4 * np.pi * L) * 10**(-6)


#Einhüllender Fit
def f(x, a, b):
    return a * np.exp(-b * x)


#Widerstand damit es zum aperiodischen Grenzfall kommt
R_ap = 3470
R_ap_theorie = np.sqrt(4*L / C)
s_R_ap = np.sqrt((1/(C*L))**2 * s_L**2 + (L/(C**3)) * s_C**2)

print(R_ap_theorie)



#Widerstand Abweichung von Theorie
a_R_ap = np.abs(R_ap_theorie - R_ap) / R_ap_theorie
print(a_R_ap)


#Resonanzfrequenz des Schwingkreises
f_res = np.sqrt(1/(L*C) - R**2/(2*L**2)) / (2*np.pi)
a_f_res = np.abs(f_res - 35000) / f_res
print(f_res)
print(a_f_res)

q_t = np.sqrt(L / (114.8**2 * C))
print("Güte = ", q_t)

print("Abweichung von q = ", (1.08-q_t)/19.14)

omega_0 = np.sqrt(1/(L * C))
print("Omega_0 = ", omega_0/(2*np.pi))
diffomega = (114.8 / L) /(2*np.pi)
print("Differenz der Omega = ", diffomega)
a_diffomega = np.abs(diffomega - 9000) / diffomega
print("Abweichung der Differenz der Omega = ", a_diffomega)
a_f_res2 = np.abs(f_res - 34000) / f_res
print("Resonanzfrequenz Abweichung = ", a_f_res2)
omega_1 = R/(2*L) + np.sqrt(R**2/(4*L**2) + 1/(L*C))
omega_2 = -R/(2*L) + np.sqrt(R**2/(4*L**2) + 1/(L*C))
print("Omegas 1 und 2 = ", omega_1/(2*np.pi), omega_2/(2*np.pi))

print(t)
print(U_ampl)
print(mu)

t_min, U_ampl_min = np.genfromtxt("einhuellende_min.txt", delimiter = ",", unpack = True)
t_max, U_ampl_max = np.genfromtxt("einhuellende_max.txt", delimiter = ",", unpack = True)
params1, cov1 = curve_fit(f, t_pos, U_ampl_pos)
b = ufloat(params1[1], np.sqrt(cov1[1, 1]))
a = ufloat(params1[0], np.sqrt(cov1[0, 0]))
x = np.linspace(0, 250)


plt.plot(t, U_ampl, "x", label = r"Messwerte der lokalen Maxima und Minima der Spannung")
plt.plot(x, f(x, *params1), "r-", label = r"Fit für alle Werte")
plt.plot(x, -f(x, *params1), "r-")
plt.plot(x, U_0 * np.exp(-2 * np.pi * mu * x), "b-", label = r"Kurve anhand der Theorie")
plt.plot(x, -U_0 * np.exp(-2 * np.pi * mu * x), "b-")
plt.xlabel(r"$\Delta t$ / $\mu$s")
plt.ylabel(r"$U_{Amplitude}$ / mV")
plt.legend(loc = "best")
plt.savefig("Spannungsamplituden.pdf")

plt.clf()

print(b/(2*np.pi))
print("Gesamtwiderstand = ", 2*L*b * 10**6)
print("T = ", 1/b)


t_2, U_C, U, phase = np.genfromtxt("SpannungFrequenz.txt", delimiter = ",", unpack = True)
U_verhältnis = U_C / U
print(U_verhältnis)


plt.plot(t_2, U_verhältnis, "x", label = r"Messdaten des Spannungsverhältnisses")
plt.xlabel(r"$f$ / kHz")
plt.ylabel(r"$\frac{U_C}{U}$")
plt.legend(loc = "best")
plt.savefig("Spannungsverhaeltnis.pdf")

plt.clf()

plt.plot(t_2, U_verhältnis, "x", label = r"Messdaten des Spannungsverhältnisses")
plt.xlabel(r"$f$ / kHz")
plt.ylabel(r"$\frac{U_C}{U}$")
plt.legend(loc = "best")
plt.xscale("log")
plt.savefig("Spannungsverhaeltnis_log.pdf")

plt.clf()

plt.plot(t_2, phase, "x", label = r"Messdaten für die Phase")
plt.xlabel(r"$f$ / kHz")
plt.ylabel(r"$\varphi$ / $\mu$ s")
plt.legend(loc = "best")
plt.savefig("Phase.pdf")

plt.clf()

plt.plot(t_2, phase, "x", label = r"Messdaten für die Phase")
plt.xlabel(r"$f$ / kHz")
plt.ylabel(r"$\varphi$ / $\mu$ s")
plt.legend(loc = "best")
plt.xscale("log")
plt.savefig("Phase_log.pdf")

plt.clf()
