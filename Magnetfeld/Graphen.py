import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

#Funktionen

#Lange Spulen
def Spule(mu_r, N, I, l):
    return const.mu_0 * mu_r * N * I / l

#Mittelpunkt Helmholtzspulen
def Helmholtz(x, N, I, R):
    return const.mu_0 * N * I * R**2 / ((R**2 + x**2)**(3/2))

#Lange Spule
xlang, Blang = np.genfromtxt('Spulelang.txt', unpack = True) #B in mT

plt.plot(xlang, Blang, "x", label = r'Magnetfeld')
plt.xlabel(r'x [m]')
plt.ylabel(r'B [mT]')
plt.legend(loc = "best")
plt.savefig('Spulelang.pdf')
plt.clf()
B_lang = Spule(1, 300, 0.68, 0.155)
print('Magnetfeldstärke der langen Spule')
print(B_lang)

#Kurze Spule
xkurz, Bkurz = np.genfromtxt('Spulekurz.txt', unpack = True) #B in mT

plt.plot(xkurz, Bkurz, "x", label = r'Magnetfeld')
plt.xlabel(r'x [m]')
plt.ylabel(r'B [mT]')
plt.legend(loc = "best")
plt.savefig('Spulekurz.pdf')
plt.clf()
B_kurz = Spule(1, 3400, 0.08, 0.09)
print('Magnetfeldstärke der kurzen Spule')
print(B_kurz)


#Helmholtzspulen

#Helmholtz A
xA, BA = np.genfromtxt('HelmholtzA.txt', unpack = True) #B in mT

plt.plot(xA, BA, "x", label = r'Magnetfeld')
plt.xlabel(r'x [m]')
plt.ylabel(r'B [mT]')
plt.legend(loc = "best")
plt.savefig('HelmholtzA.pdf')
plt.clf()
B_A = Helmholtz(0.05, 100, 1.94, 0.0625)
print('Magnetfeldstärke im Mittelpunkt zwischen den zwei Spulen A')
print(B_A)

#Helmholtz B
xB, BB = np.genfromtxt('HelmholtzB.txt', unpack = True) #B in mT

plt.plot(xB, BB, "x", label = r'Magnetfeld')
plt.xlabel(r'x [m]')
plt.ylabel(r'B [mT]')
plt.legend(loc = "best")
plt.savefig('HelmholtzB.pdf')
plt.clf()
B_B = Helmholtz(0.075, 100, 1.94, 0.0625)
print('Magnetfeldstärke im Mittelpunkt zwischen den zwei Spulen B')
print(B_B)

#Helmholtz C
xC, BC = np.genfromtxt('HelmholtzC.txt', unpack = True) #B in mT

plt.plot(xC, BC, "x", label = r'Magnetfeld')
plt.xlabel(r'x [m]')
plt.ylabel(r'B [mT]')
plt.legend(loc = "best")
plt.savefig('HelmholtzC.pdf')
plt.clf()
B_C = Helmholtz(0.1, 100, 1.94, 0.0625)
print('Magnetfeldstärke im Mittelpunkt zwischen den zwei Spulen C')
print(B_C)


#Hysteresekurve der Ringspule
xRing, BRing = np.genfromtxt('Hysterese.txt', unpack = True) #B in mT

#H-Feld 
H = 595 * xRing / (2 * np.pi * 0.1325) 
print(H)
plt.plot(H[0:11], BRing[0:11], "yx", label = r'Neukurve')
plt.plot(H[11:], BRing[11:], "bx", label = r'Hysteresekurve')
plt.xlabel(r'H [A/m]')
plt.ylabel(r'B [mT]')
plt.legend(loc = "best")
plt.grid()
plt.savefig('Hysterese.pdf')

plt.clf()
