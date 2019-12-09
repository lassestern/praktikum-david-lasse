import numpy as np


T_k = np.array([76.0, 99.4, 73.3, 78.1, 78.3, 77.4, 80.0]) + 273.15  #Temperatur des erhitzten Körpers
T_w = np.array([21.9, 22.4, 21.9, 21.7, 21.4, 21.5, 21.4]) + 273.15  #Temperatur des Wasser im Dewar-Gefäß (davor)
T_m = np.array([23.1, 26.6, 22.9, 24.7, 24.5, 24.4, 23.2]) + 273.15  #Mischtemperatur im Dewar-Gefäß

m_w = np.array([0.56288, 0.56416, 0.56078, 0.56803, 0.57302, 0.58335, 0.56694])  #Masse des Wasser im Dewar-Gefäß
m_k = np.array([0.11279, 0.11279, 0.11279, 0.23645, 0.23645, 0.23645, 0.1076])

c_w = 4186  #spezifische Wärmekapazität von Wasser


#Wärmakapazität des Dewar-Gefäßes bestimmen
T_misch = 43.1 + 273.15  #Mischtemperatur
T_y = 67.5 + 273.15  #Temperatur des erhitzten Wassers
T_x = 21.3 + 273.15  #Temperatur des Wasser im Dewar-Gefäß (davor)
m_y = 0.28971
m_x = 0.26010
C = (c_w * m_y * (T_y - T_misch) - c_w * m_x * (T_misch - T_x)) / (T_misch - T_x)

print("Wärmekapazität des Dewar-Gefäßes:")
print(C)


#spezifische Wärmekapazität der verschiedenen Materialien

c_k = ((c_w * m_w + C) * (T_m - T_w)) / (m_k * (T_k - T_m))

print("Spezifische Wärmekapazitäten für Aluminium (1, 2, 3), Kupfer (4, 5, 6) und Graphit (7):")
print(c_k)


#molare Wärmekapazität(Molwärme) bei konstantem Druck

M = np.array([0.027, 0.027, 0.027, 0.0635, 0.0635, 0.0635, 0.012])

C_p = c_k * M

print("Molwärme bei konstantem Druck:")
print(C_p)


#Daraus Wärmekapazität bei konstantem Volumen berechnen

alpha = np.array([23.5, 23.5, 23.5, 16.8, 16.8, 16.8, 8]) * 10**-6
k = np.array([75, 75, 75, 136, 136, 136, 33]) * 10**9
V_0 = np.array([10**-5, 10**-5, 10**-5, 7.09*10**-6, 7.09*10**-6, 7.09*10**-6, 5.33*10**-6])

C_v = C_p - 9 * alpha**2 * k * V_0 * T_m

print("Molwärme bei konstantem Volumen:")
print(C_v)

#Mittelwert der Molwärme berechnen

C_Mittelwert_al = np.sum(C_v[0:2]) / 3
C_Mittelwert_cu = np.sum(C_v[3:5]) / 3
C_gr = C_v[6]

print("Mittelwert der Molwärme bei konstantem Druck:")
print(C_Mittelwert_al)
print(C_Mittelwert_cu)
print(C_gr)
print((C_Mittelwert_al+C_Mittelwert_cu+C_gr)/3)
print(np.sum(C_v) / len(C_v))