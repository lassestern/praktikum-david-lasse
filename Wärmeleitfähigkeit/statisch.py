import io
import numpy as np
import matplotlib.pyplot as plt

with io.open('GLXportRun1.txt', 'r', encoding = 'UTF-16') as f:
    Messung, T1, T2, T3, T4, T5, T6, T7, T8, t = np.genfromtxt(f, unpack = True)

plt.plot(t, T1, "-", label =r'Messing Außen breit')
plt.plot(t, T4, "-", label =r'Messing Außen dünn')
plt.plot(t, T5, "-", label =r'Alumminium außen')
plt.plot(t, T8, "-", label =r'Edelstahl außen')
plt.xlabel(r"Zeit")
plt.ylabel(r"Temperatur")
plt.legend(loc = "best")
plt.show()
plt.savefig("Tstatisch.pdf")
plt.close
plt.clf()

plt.plot(t, T7-T8, "-", label =r"Temperaturdifferenz Edelstahl")
plt.plot(t, T2-T1, "-", label =r"Temperaturdifferenz Messing")
plt.xlabel(r"Zeit")
plt.ylabel(r"Temperaturdifferenz")
plt.legend(loc = "best")
plt.show()
plt.savefig("diffstatisch.pdf")
plt.close
plt.clf()


#Wärmestrom

def Wärmestrom(kappa, Fläche, Tdiff):
    return -kappa * Fläche / Tdiff

#Aluminium
print('Wärmestom Alu')
i=1
while i<6:
    Tdiff = abs(T5[i*30]-T6[i*30])
    #print(Tdiff)
    print(Wärmestrom(220, 0.012*0.004, Tdiff))
    i = i +1

#Edelstahl
print('Wärmestom Edelstahl')
i=1
while i<6:
    Tdiff = abs(T7[i*30]-T8[i*30])
    #print(Tdiff)
    print(Wärmestrom(21, 0.012*0.004, Tdiff))
    i = i +1

#Messing breit
print('Wärmestom Messing breit')
i=1
while i<6:
    Tdiff = abs(T1[i*30]-T2[i*30])
    #print(Tdiff)
    print(Wärmestrom(105, 0.012*0.004, Tdiff))
    i = i +1

#Messing dünn
print('Wärmestom Messing dünn')
i=1
while i<6:
    Tdiff = abs(T3[i*30]-T4[i*30])
    #print(Tdiff)
    print(Wärmestrom(105, 0.007*0.004, Tdiff))
    i = i +1