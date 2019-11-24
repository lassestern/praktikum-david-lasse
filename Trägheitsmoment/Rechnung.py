import numpy as np

#Aufgabe 1.1
r = 0.2

phi_grad, phi_rad, F = np.genfromtxt('D_Feder.txt', unpack = True)

for c in phi_rad:

    D = F * r / phi_rad

print("Gemessene Winkelrichtgrößen:")
print(D)

D_m = np.sum(D)/len(phi_rad)

print("Gemittelte Winkelrichtgröße:")
print(D_m)

#Aufgabe 1.2

r = 0.0405/2
h = 0.0204
m = 0.262

I_S = m*((r**2)/4 + (h**2)/12)  #Trägheitsmoment des Zylinders zum Schwerpunkt
print("Trägheitsmoment des kleinen Zylinders durch Schwerpunkt:")
print(I_S)

a, T = np.genfromtxt("I_Drill.txt", unpack = True)

for abstand, periode in zip(a, T):
    I_K = I_S + m*(a**2)  #Trägheitsmoment des Zylinders zur Drehachse

print("Trägheitsmoment des kleinen Zylinders:")
print(I_K)

for abstand, periode in zip(a, T):
    I_D = (T**2 * D_m)  / (4 * np.pi**2) - 2*I_K  #Trägheitsmoment der Drillachse

print("Gemessene Trägheitsmomente der Drillachse:")
print(I_D)

I_Dm = np.sum(I_D)/len(I_D)

print("Gemitteltes Trägheitsmoment der Drillachse:")
print(I_Dm)

#Aufgabe 2.1
T_1 = np.genfromtxt("T_zyli.txt", unpack = True)

T_1m = np.sum(T_1)/len(T_1)
I_1m = (T_1m**2 * D_m)  / (4 * np.pi**2)

print("Gemitteltes Trägheitsmoment des Zylinders durch Schwerpunkt:")
print(I_1m)

#Aufgabe 2.2
T_2 = np.genfromtxt("T_Kugel.txt", unpack = True)

T_2m = np.sum(T_2)/len(T_2)
I_2m = (T_2m**2 * D_m)  / (4 * np.pi**2)

print("Gemitteltes Trägheitsmoment der Kugel durch Schwerpunkt:")
print(I_2m)

I_D_linR = (D_m*4.99758)/(4*np.pi**2) - 2*I_S
print("Trägheitsmoment der Drillachse anhand der lin. Regression berechnen:")
print(I_D_linR)
