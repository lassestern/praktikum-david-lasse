import numpy as np

#Aufgabe 1.1
r = 0.2

phi_grad, phi_rad, F = np.genfromtxt('D_Feder.txt', unpack = True)

for c in phi_rad:

    D = F * r / phi_rad

"""print("Gemessene Winkelrichtgrößen:")
print(D)"""

D_m = np.sum(D)/len(phi_rad)

print("Gemittelte Winkelrichtgröße:")
print(D_m)

#Standardabweichung des Mittelwerts der Winkelrichtgröße
a = (D - D_m)**2
s_Dm = np.sqrt(np.sum(a) / 90)

print("Standardabweichung des Mittelwerts der Winkelrichtgröße:")
print(s_Dm)


######################################################
#Aufgabe 1.2

r = 0.0405/2
h = 0.0204
m = 0.262

#Trägheitsmoment der Drillachse anhand der lin. Regression berechnen
I_S = m*((r**2)/4 + (h**2)/12)  #Trägheitsmoment des Zylinders zum Schwerpunkt
I_D_linR = (D_m*4.99758)/(4*np.pi**2) - 2*I_S
print("Trägheitsmoment der Drillachse anhand der lin. Regression berechnen:")
print(I_D_linR)

#Fehler des Trägheitsmomentes der Drillachse
s_I_D_linR = np.sqrt((D_m/(4*np.pi**2) * 0.602625)**2 + (4.99758/(4*np.pi**2) * s_Dm)**2)
print("Fehler des Trägheitsmomentes der Drillachse:")
print(s_I_D_linR)


"""I_S = m*((r**2)/4 + (h**2)/12)  #Trägheitsmoment des Zylinders zum Schwerpunkt
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

#Standardabweichung des Mittelwerts des Trägheitsmoments der Drillachse
b = (I_D - I_Dm)**2
s_I_Dm = np.sqrt(np.sum(b) / 90)

print("Standardabweichung des Mittelwerts des Trägheitsmoments der Drillachse:")
print(s_I_Dm)"""

#########################################################
#Aufgabe 2.1
T_1 = np.genfromtxt("T_zyli.txt", unpack = True)

T_1m = np.sum(T_1)/len(T_1)
I_1m = (T_1m**2 * D_m)  / (4 * np.pi**2) - I_D_linR

print("Gemitteltes Trägheitsmoment des Zylinders durch Schwerpunkt:")
print(I_1m)

#Standardabweichung des Mittelwerts der Periode des Zylinders
c = (T_1 - T_1m)**2
s_T_1m = np.sqrt(np.sum(c) / 20)

print("Standardabweichung des Mittelwerts der Periode des Zylinders:")
print(s_T_1m)

#Fehler des Trägheitsmoments des Zylinders
s_I_1m = np.sqrt((D_m*T_1m/(2*np.pi**2) * s_T_1m)**2 + (T_1m**2/(4*np.pi**2) * s_Dm)**2)

print("Fehler des Trägheitsmoments des Zylinders:")
print(s_I_1m)


#########################################################
#Aufgabe 2.2
T_2 = np.genfromtxt("T_Kugel.txt", unpack = True)

T_2m = np.sum(T_2)/len(T_2)
I_2m = (T_2m**2 * D_m)  / (4 * np.pi**2) - I_D_linR

print("Gemitteltes Trägheitsmoment der Kugel durch Schwerpunkt:")
print(I_2m)

#Standardabweichung des Mittelwerts der Periode der Kugel
d = (T_2 - T_2m)**2
s_T_2m = np.sqrt(np.sum(d) / 20)

print("Standardabweichung des Mittelwerts der Periode der Kugel:")
print(s_T_2m)

#Fehler des Trägheitsmoments der Kugel
s_I_2m = np.sqrt((D_m*T_2m/(2*np.pi**2) * s_T_2m)**2 + (T_2m**2/(4*np.pi**2) * s_Dm)**2)

print("Fehler des Trägheitsmoments der Kugel:")
print(s_I_2m)


###########################################################
#Aufgabe 3
T_3 = np.genfromtxt("T_posa.txt", unpack = True)

T_3m = np.sum(T_3)/len(T_2)
I_3m = (T_3m**2 * D_m)  / (4 * np.pi**2) - I_D_linR

print("Trägheitsmoment der Puppe in Position A:")
print(I_3m)

#Standardabweichung des Mittelwerts der Periode der Puppe in Pos A
e = (T_3 - T_3m)**2
s_T_3m = np.sqrt(np.sum(e) / 20)

#Fehler des Trägheitsmoments der Kugel
s_I_3m = np.sqrt((D_m*T_3m/(2*np.pi**2) * s_T_3m)**2 + (T_3m**2/(4*np.pi**2) * s_Dm)**2)

print("Fehler des Trägheitsmoments der Puppe in Pos A:")
print(s_I_3m)


T_4 = np.genfromtxt("T_posb.txt", unpack = True)

T_4m = np.sum(T_4)/len(T_2)
I_4m = (T_4m**2 * D_m)  / (4 * np.pi**2) - I_D_linR

print("Trägheitsmoment der Puppe in Position B:")
print(I_4m)

#Standardabweichung des Mittelwerts der Periode der Puppe in Pos B
f = (T_4 - T_4m)**2
s_T_4m = np.sqrt(np.sum(f) / 20)

#Fehler des Trägheitsmoments der Kugel
s_I_4m = np.sqrt((D_m*T_4m/(2*np.pi**2) * s_T_4m)**2 + (T_4m**2/(4*np.pi**2) * s_Dm)**2)

print("Fehler des Trägheitsmoments der Puppe in Pos B:")
print(s_I_4m)


#Theoretisch ausgerechnetes Trägheitsmoment der Puppe
r_kopf = 0.0152
m_kopf = 0.00956
r_torso = 0.02025
l_torso = 0.0981
m_torso = 0.0821
r_bein = 0.00835
l_bein = 0.1705
a_bein = 0.01
m_bein = 0.0243
r_arm = 0.00705
l_arm = 0.135
a_arm1 = 0.027
a_arm2 = 0.0905
m_arm = 0.0137

I_kopf = 2/5 * m_kopf * r_kopf**2
I_torso = (m_torso * r_torso**2)/2
I_bein = m_bein * ((r_bein**2)/2 + a_bein**2)
I_arm1 = m_arm * ((r_arm**2)/2 + a_arm1**2)
I_arm2 = m_arm * ((r_arm**2)/4 + (l_arm**2)/12 + a_arm2**2)

"""print("Berechnete Trägheitsmomente der Puppe:")
print(I_kopf)
print(I_torso)
print(I_bein)
print(I_arm1)
print(I_arm2)"""

I_posa = I_kopf + I_torso + 2*I_bein + 2*I_arm1
I_posb = I_kopf + I_torso + 2*I_bein + 2*I_arm2

print("Theoretisch berechnetes Trägheitsmoment der Puppe in Position A:")
print(I_posa)
print("Theoretisch berechnetes Trägheitsmoment der Puppe in Position B:")
print(I_posb)

print("Summe Fehler:")
print(s_I_1m + s_I_D_linR)
print(s_I_2m + s_I_D_linR)
print(s_I_3m + s_I_D_linR)
print(s_I_4m + s_I_D_linR)


