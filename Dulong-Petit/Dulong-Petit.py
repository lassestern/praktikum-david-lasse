import numpy as np


T_k = np.array([76.0, 99.4, 73.3, 78.1, 78.3, 77.4, 80.0]) + 273.15  #Temperatur des erhitzten Körpers
T_w = np.array([21.9, 22.4, 21.9, 21.7, 21.4, 21.5, 21.4]) + 273.15  #Temperatur des Wasser im Dewar-Gefäß (davor)
T_m = np.array([23.1, 26.6, 22.9, 24.7, 24.5, 24.4, 23.2]) + 273.15  #Mischtemperatur im Dewar-Gefäß
T_m_mittel = np.array([np.sum(T_m[0:3]) / 3, np.sum(T_m[3:6]) / 3, T_m[6]])

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


#Gemittelte spezifische Wärmekapazität der verschiedenen Materialien

c_k_mittel = np.array([np.sum(c_k[0:3]) / 3, np.sum(c_k[3:6]) / 3, c_k[6]])

print("Gemittlete spezifische Wärmekapazitäten für Aluminium (1), Kupfer (2) und Graphit (3):")
print(c_k_mittel)


#Standardabweichungen der Mittelwerte der spezifischen Wärmekapazität

s_c_k_al = np.sqrt(((c_k_mittel[0] - c_k[0])**2 + (c_k_mittel[0] - c_k[1])**2 + (c_k_mittel[0] - c_k[2])**2) / 6)
s_c_k_cu = np.sqrt(((c_k_mittel[1] - c_k[3])**2 + (c_k_mittel[1] - c_k[4])**2 + (c_k_mittel[1] - c_k[5])**2) / 6)

print("Standardabweichungen der Mittelwerte der spezifischen Wärmekapazität:")
print(s_c_k_al)
print(s_c_k_cu)


#Standardabweichungen der Mittelwerte der Mischtemperatur

s_T_m_al = np.sqrt(((T_m_mittel[0] - T_m[0])**2 + (T_m_mittel[0] - T_m[1])**2 + (T_m_mittel[0] - T_m[2])**2) / 6)
s_T_m_cu = np.sqrt(((T_m_mittel[1] - T_m[3])**2 + (T_m_mittel[1] - T_m[4])**2 + (T_m_mittel[1] - T_m[5])**2) / 6)

print("Standardabweichungen der Mittelwerte der Mischtemperatur:")
print(s_T_m_al)
print(s_T_m_cu)


#Gemittelte molare Wärmekapazität(Molwärme) bei konstantem Druck

M = np.array([0.027, 0.0635, 0.012])

C_p = c_k_mittel * M

print("Gemittelte Molwärme bei konstantem Druck:")
print(C_p)


#Fehlerfortpflanzung für die gemittelte molare Wärmekapazität bei konstantem Druck

s_C_p_al = s_c_k_al * M[0]
s_C_p_cu = s_c_k_cu * M[1]

print("Fehlerfortpflanzung für die gemittelte molare Wärmekapazität bei konstantem Druck:")
print(s_C_p_al)
print(s_C_p_cu)


#Daraus gemittelte Molwärme bei konstantem Volumen berechnen

alpha = np.array([23.5, 16.8, 8]) * 10**-6
k = np.array([75, 136, 33]) * 10**9
V_0 = np.array([10**-5, 7.09*10**-6, 5.33*10**-6])

C_v = C_p - 9 * alpha**2 * k * V_0 * T_m_mittel

print("Gemittlete Molwärme bei konstantem Volumen:")
print(C_v)


#Fehlerfortpflanzung für die gemittelte Molwärme bei konstantem Volumen

s_C_v_al = np.sqrt((s_C_p_al)**2 + (9 * alpha[0]**2 * k[0] * V_0[0])**2 * (s_T_m_al)**2)
s_C_v_cu = np.sqrt((s_C_p_cu)**2 + (9 * alpha[1]**2 * k[1] * V_0[1])**2 * (s_T_m_cu)**2)

print("Fehlerfortpflanzung für die gemittelte Molwärme bei konstantem Volumen:")
print(s_C_v_al)
print(s_C_v_cu)







"""#Mittelwert der Molwärme berechnen

C_Mittelwert_al = C_v[0]
C_Mittelwert_cu = C_v[1]
C_gr = C_v[2]

print("Mittelwert der Molwärme bei konstantem Druck:")
print(C_Mittelwert_al)
print(C_Mittelwert_cu)
print(C_gr)


#Standardabweichung der Mittelwerte

s_al = np.sqrt(((C_Mittelwert_al - C_v[0])**2 + (C_Mittelwert_al - C_v[1])**2 + (C_Mittelwert_al - C_v[2])**2) / 6)

s_cu = np.sqrt(((C_Mittelwert_cu - C_v[3])**2 + (C_Mittelwert_cu - C_v[4])**2 + (C_Mittelwert_cu - C_v[5])**2) / 6)

print("Standardabweichungen:")
print(s_al)
print(s_cu)"""







