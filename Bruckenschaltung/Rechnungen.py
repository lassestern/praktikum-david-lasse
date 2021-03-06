import numpy as np
import matplotlib.pyplot as plt


#Formel für den Mittelwert
def Mittel(x):
    return np.sum(x) / len(x)

#Formel für die Standardabweichung des Mittelwerts
def stanni(Zahlen, Mittelwert):
    i=0
    s=0
    n=len(Zahlen)
    while i<len(Zahlen):
        s = s + (Zahlen[i] - Mittelwert)**2
        i = i + 1
    return np.sqrt(s/(n*(n-1)))


#Wheaton
print('Wheaton')
def Wheaton(R2, R3, R4):
    return R2 * R3 / R4

print('Wert14')
#Wert 14

R_2 = np.array([1000, 664, 332])
R_3 = np.array([472, 573, 730])
R_4 = np.array([528, 427, 270])

R_x_14 = Wheaton(R_2, R_3, R_4)
Mittel14 = Mittel(R_x_14)
Mittel14Fehler = stanni(R_x_14, Mittel14)
R_x_14_prozfehler = np.sqrt(0.002**2 + 0.005 **2 + 0.005**2)
R_x_14_fehler = Mittel14 * R_x_14_prozfehler

print('R14')
print(R_x_14)
print('MittelR14')
print(Mittel14)
print('Fehler1')
print(Mittel14Fehler)
print('Fehler2')
print(R_x_14_fehler)

print('Wert13')
#Wert 13

R_2_13 = np.array([1000, 664, 332])
R_3_13 = np.array([236, 323, 489])
R_4_13 = np.array([764, 677, 511])

R_x_13 = Wheaton(R_2_13, R_3_13, R_4_13)
Mittel13 = Mittel(R_x_13)
Mittel13Fehler = stanni(R_x_13, Mittel13)
R_x_13_prozfehler = np.sqrt(0.002**2 + 0.005 **2 + 0.005**2)
R_x_13_fehler = Mittel13 * R_x_13_prozfehler


print('R13')
print(R_x_13)
print('MittelR13')
print(Mittel13)
print('Fehler1')
print(Mittel13Fehler)
print('Fehler2')
print(R_x_13_fehler)


#Kapazitätsbrücke

print('Kapazität')

def cap(C2, R4, R3):
    return C2 * 10**(-9) * R4 / R3

#Für den Widerstabd kann wieder die Funktion "Wheaton" genutzt werden

#Wert9
print('Wert9')

C_2_9 = np.array([399, 597, 992]) # in nF
R_2_9 = np.array([500, 339, 204])
R_3_9 = np.array([480, 580, 693])
R_4_9 = np.array([520, 420, 307])

R_x_9 = Wheaton(R_2_9, R_3_9, R_4_9)
MittelR9 = Mittel(R_x_9)
MittelR9Fehler = stanni(R_x_9, MittelR9)
R_x_9_prozfehler = np.sqrt(0.03**2 + 0.005 **2 + 0.005**2)
R_x_9_fehler = MittelR9 * R_x_9_prozfehler

C_x_9 = cap(C_2_9, R_4_9, R_3_9)
MittelC9 = Mittel(C_x_9)
MittelC9Fehler = stanni(C_x_9, MittelC9)
C_x_9_prozfehler = np.sqrt(0.002**2 + 0.005 **2 + 0.005**2)
C_x_9_fehler = MittelC9 * C_x_9_prozfehler

print('R9')
print(R_x_9)
print('MittelR9')
print(MittelR9)
print('Fehler1')
print(MittelR9Fehler)
print('Fehler2')
print(R_x_9_fehler)
print('C9')
print(C_x_9)
print('MittelC9')
print(MittelC9)
print('Fehler1')
print(MittelC9Fehler)
print('Fehler2')
print(C_x_9_fehler)




#Induktivitätsbrücke

def ind(L2, R3, R4):
    return L2 * 10**(-3) * R3 / R4

#Wert16 Induktionsbrücke
print('Wert16')

L_2_16 = np.array([27.5, 14.6]) # in mH
R_2_16 = np.array([122, 115])
R_3_16 = np.array([757, 789])
R_4_16 = np.array([243, 211])

R_x_16 = Wheaton(R_2_16, R_3_16, R_4_16)
MittelR16 = Mittel(R_x_16)
MittelR16Fehler = stanni(R_x_16, MittelR16)
R_x_16_prozfehler = np.sqrt(0.03**2 + 0.005 **2 + 0.005**2)
R_x_16_fehler = MittelR16 * R_x_16_prozfehler

L_x_16 = ind(L_2_16, R_3_16, R_4_16)
MittelL16 = Mittel(L_x_16)
MittelL16Fehler = stanni(L_x_16, MittelL16)
L_x_16_prozfehler = np.sqrt(0.002**2 + 0.005 **2 + 0.005**2)
L_x_16_fehler = MittelL16 * L_x_16_prozfehler

print('R16')
print(R_x_16)
print('MittelR16')
print(MittelR16)
print('Fehler1')
print(MittelR16Fehler)
print('Fehler2')
print(R_x_16_fehler)
print('L16')
print(L_x_16)
print('MittelL16')
print(MittelL16)
print('Fehler1')
print(MittelL16Fehler)
print('Fehler2')
print(L_x_16_fehler)


#Maxwellbrücke

def indmaxwell(R2, R3, C4):
    return R2 * R3 * C4 * 10**(-9)

#Wert16 Maxwellbrücke
print('Wert16 Maxwellbrücke')

C_4_16max = np.array([399, 399, 399, 450]) # in nF
R_2_16max = np.array([1000, 332, 664, 332])
R_3_16max = np.array([293, 557, 386, 555])
R_4_16max = np.array([707, 443, 614, 445])
omega = 21.9

R_x_16max = Wheaton(R_2_16max, R_3_16max, R_4_16max)
MittelR16max = Mittel(R_x_16max)
R_x_16_prozfehler2 = np.sqrt(0.03**2 + 0.03 **2 + 0.03**2)
R_x_16_fehler2 = MittelR16 * R_x_16_prozfehler2


L_x_16max = indmaxwell(R_2_16max, R_3_16max, C_4_16max)
MittelL16max = Mittel(L_x_16max)
MittelL16Fehlermax = stanni(L_x_16max, MittelL16max)
L_x_16_prozfehlermax = np.sqrt(0.002**2 + 0.03 **2 + 0.03**2)
L_x_16_fehlermax = MittelL16max * L_x_16_prozfehlermax

print('R16max')
print(R_x_16max)
print('MittelR16max')
print(MittelR16max)
print('Fehler1')
print(MittelR16Fehler)
print('Fehler2')
print(R_x_16_fehler2)
print('L16max')
print(L_x_16max)
print('MittelL16max')
print(MittelL16max)
print('Fehler1')
print(MittelL16Fehlermax)
print('Fehler2')
print(L_x_16_fehlermax)




#Wienrobinsonbrücke



v, U = np.genfromtxt('Wienrobinsonwerte.txt', unpack = True) #U in mV
v_0 = 241 # Hz
U_s = 0.5

x = np.linspace(0, 2.5, 21)

#Frequenzverhältnis
omega = v / v_0
#Effektive Brückenspannung
U_eff = U * 10**(-3) / (2*np.sqrt(2))
#Spannungsverhältnis
U_rel = U_eff / U_s
#Theoretisches Spannungsverhältnis
U_reltheo = np.sqrt((omega**2-1)**2 / (9 * (1 - omega**2)**2 + 9 * omega**2)) 


#params, covariance_matrix = np.polyfit(omega, U_reltheo, deg = 3, cov = True) 
#fit = params[0]*x**3 + params[1]*x**2 + params[2]*x + params[3] 




plt.plot(omega, U_rel, 'x', label = r'Messwerte')
plt.plot(omega, U_reltheo, "-", label = r'Theoriekurve')
plt.xlabel(r'$\nu / \nu _0$')
plt.ylabel(r'$U_{Br} /  U_S $')
plt.legend(loc = "best")
plt.savefig("Brücke.pdf")






#Klirrfaktor berechnen

f2 = np.sqrt((2**2-1)**2 / (9 * (1 - 2**2)**2 + 9 * 2**2))
U_2 = 0.004 / f2
k = U_2 / U_s

print('Klirrfaktor')
print(k)
print(f2)
print(U_2)
