import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt


#### mittlere freie Weglänge ###############################################################################################################
w_30085 = 0.0029/(5.5*10**7*np.exp(-6876/300.85))       #mittlere freie Weglänge bei einer Temp von 300,85 Kelvin
w_42415 = 0.0029/(5.5*10**7*np.exp(-6876/424.15))       #mittlere freie Weglänge bei einer Temp von 425,15 Kelvin
w_44315 = 0.0029/(5.5*10**7*np.exp(-6876/443.15))       #mittlere freie Weglänge bei einer Temp von 443,15 Kelvin
w_47025 = 0.0029/(5.5*10**7*np.exp(-6876/470.25))       #mittlere freie Weglänge bei einer Temp von 470,25 Kelvin

rel_30085 = 0.01/w_30085                                #Verhältnis zwischen Abstand Glühdraht und Anode bei 300,85 Kelvin
rel_42415 = 0.01/w_42415                                #Verhältnis zwischen Abstand Glühdraht und Anode bei 425,15 Kelvin
rel_44315 = 0.01/w_44315                                #Verhältnis zwischen Abstand Glühdraht und Anode bei 443,15 Kelvin
rel_47025 = 0.01/w_47025                                #Verhältnis zwischen Abstand Glühdraht und Anode bei 470,25 Kelvin

print(f"""
mittlere freie Weglängen
300,85K: {w_30085}
424,15K: {w_42415}
443,15K: {w_44315}
470,25K: {w_47025}
Verhältnis a/w
300,85K: {rel_30085}
424,15K: {rel_42415}
443,15K: {rel_44315}
470,25K: {rel_47025}
""")
#### Aufgabenteil a ########################################################################################################################
x_Skala1 = np.genfromtxt("x_Skala1.txt", unpack = True) 
x_Skala2 = np.genfromtxt("x_Skala2.txt", unpack = True)
U_Skala1 = (np.sum(5/x_Skala1)/len(x_Skala1))              #Volt pro Kästchen
U_Skala2 = (np.sum(5/x_Skala2)/len(x_Skala2))              #Volt pro Kästchen

deltay1, deltax1, xpos1 = np.genfromtxt("steigung1.txt", unpack = True)
Steigung1 = deltay1/deltax1
U1 = xpos1*U_Skala1

plt.plot(U1, Steigung1, r'x', label=r"Betrag")
plt.xlabel(r"Bremsspannung [V]")
plt.ylabel(r"|Steigung|")
plt.legend(loc = "best")
plt.savefig("Steigung1.pdf")
plt.clf()

deltay2, deltax2, xpos2 = np.genfromtxt("steigung2.txt", unpack = True)
Steigung2 = deltay2/deltax2 
U2 = xpos2*U_Skala2
print(Steigung2, deltay2)
plt.plot(U2, Steigung2, r'gx', label=r"Betrag")
plt.xlabel(r"Bremsspannung [V]")
plt.ylabel(r"|Steigung|")
plt.legend(loc = "best")
plt.savefig("Steigung2.pdf")
plt.clf()




#### Aufgabenteil b ########################################################################################################################
K_d = np.genfromtxt("MaximaAbstand.txt", unpack = True)   #Abstand der Maxima in der Einheit Kästchen
x_Skala = np.genfromtxt("xSkala.txt", unpack = True)      #Werte zur Berechnung der x-Skala, Kästchen pro 5V

U_Skala = (np.sum(5/x_Skala)/len(x_Skala))              #Volt pro Kästchen
U_d = K_d * U_Skala                                     #Berechnung des Abstands der Maxima in Volt
deltaE = const.e * U_d                                  #Berechnung der Anregungsenergie vom Grundzustand in den ersten angeregten Zustand
deltalambda = const.c * const.h /deltaE                 #Berechnung der Wellenlänge, die beim Übergang in den Grundzustand emmitiert wird

print(f""" 
Volt pro Kästchen: {U_Skala}
Abstand der Maxima in V: {U_d}
Anregungsenergie in eV: {U_d}
Wellenlänge in m: {deltalambda}
""")

def Mittel(x):
    return sum(x)/len(x)

print(f""" 
Mittelwerte
Abstand der Maxima in V: {Mittel(U_d)}
Anregungsenergie in eV: {Mittel(U_d)}
Wellenlänge in m: {Mittel(deltalambda)}
""")