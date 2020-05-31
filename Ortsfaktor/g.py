import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const


def Freifall(s, t):
    return 2*s/(t**2)

def Schief(s, t, h):
    return 2*s/(t**2*h/1.2)

def Mittel(Werte):
    return np.sum(Werte)/len(Werte)

#Formel für die Standardabweichung des Mittelwerts
def stanni(Zahlen, Mittelwert):
    i=0
    s=0
    n=len(Zahlen)
    while i<len(Zahlen):
        s = s + (Zahlen[i] - Mittelwert)**2
        i = i + 1
    return np.sqrt(s/(n*(n-1)))

#Freier Fall

t1, t2, t3 = np.genfromtxt('freifall.txt', unpack = True) #Fallzeiten in Sekunden

#70,6cm
g7 = Freifall(0.706, t1)
g7mittel = Mittel(g7)
g7stanni = stanni(g7, g7mittel)
print("Mittelwert 70,6cm")
print(g7mittel)
print("zugehörige Standardabweichung")
print(g7stanni)

#103,6cm
g8 = Freifall(1.036, t2)
g8mittel = Mittel(g8)
g8stanni = stanni(g8, g8mittel)
print("Mittelwert 103,6cm")
print(g8mittel)
print("zugehörige Standardabweichung")
print(g8stanni)

#141,5cm
g9 = Freifall(1.415, t3)
g9mittel = Mittel(g9)
g9stanni = stanni(g9, g9mittel)
print("Mittelwert 141,5cm")
print(g9mittel)
print("zugehörige Standardabweichung")
print(g9stanni)



#Schiefe Ebene

V1, V2, V3, V4, V5, V6 = np.genfromtxt('ebene.txt', unpack = True) #Fallzeiten in Sekunden

#V1: 10,09°
s1=0.78  
h1=0.21
g1 = Schief(s1, V1, h1)
g1mittel = Mittel(g1)
g1stanni = stanni(g1, g1mittel)
print("Mittelwert 10,09° 78cm")
print(g1mittel)
print("zugehörige Standardabweichung")
print(g1stanni)

#V2: 10,09°
s2=0.303  
h1=0.21
g2 = Schief(s2, V2, h1)
g2mittel = Mittel(g2)
g2stanni = stanni(g2, g2mittel)
print("Mittelwert 10,09° 30,3cm")
print(g2mittel)
print("zugehörige Standardabweichung")
print(g2stanni)

#V3: 15,47°
s1=0.78  
h3=0.32
g3 = Schief(s1, V3, h3)
g3mittel = Mittel(g3)
g3stanni = stanni(g3, g3mittel)
print("Mittelwert 15,47° 78cm")
print(g3mittel)
print("zugehörige Standardabweichung")
print(g3stanni)

#V4: 15,47°
g4 = Schief(s2, V4, h3)
g4mittel = Mittel(g4)
g4stanni = stanni(g4, g4mittel)
print("Mittelwert 15,47° 30,3cm")
print(g4mittel)
print("zugehörige Standardabweichung")
print(g4stanni)

#V5: 5,02°
h5=0.105
g5 = Schief(s2, V5, h5)
g5mittel = Mittel(g5)
g5stanni = stanni(g5, g5mittel)
print("Mittelwert 5,02° 30,3cm")
print(g5mittel)
print("zugehörige Standardabweichung")
print(g5stanni)

#V6: 5,02°
g6 = Schief(s1, V6, h5)
g6mittel = Mittel(g6)
g6stanni = stanni(g6, g6mittel)
print("Mittelwert 5,02° 78cm")
print(g6mittel)
print("zugehörige Standardabweichung")
print(g6stanni)


#Plots freier Fall
g = const.g
g_plot = np.array([g, g])
xg = np.array([-1, 20])
x=np.linspace(0, 20, 20)
plt.axis([0, 20, 3, 11])
plt.plot( x, g9,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("1415.pdf")
plt.clf()

plt.axis([0, 20, 3, 11])
plt.plot( x, g8,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("1036.pdf")
plt.clf()

plt.axis([0, 20, 3, 11])
plt.plot( x, g7,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("706.pdf")
plt.clf()


#Plots schiefe Ebene

x2 = np.linspace(0, 10, 10)
plt.axis([0, 10, 3, 11])
plt.plot( x2, g1,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("10_s1.pdf")
plt.clf()

x2 = np.linspace(0, 10, 10)
plt.axis([0, 10, 3, 11])
plt.plot( x2, g2,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("10_s2.pdf")
plt.clf()

x2 = np.linspace(0, 10, 10)
plt.axis([0, 10, 3, 11])
plt.plot( x2, g3,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("15_s1.pdf")
plt.clf()

x2 = np.linspace(0, 10, 10)
plt.axis([0, 10, 3, 11])
plt.plot( x2, g4,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("15_s2.pdf")
plt.clf()

x2 = np.linspace(0, 10, 10)
plt.axis([0, 10, 3, 11])
plt.plot( x2, g5,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("5_s2.pdf")
plt.clf()

x2 = np.linspace(0, 10, 10)
plt.axis([0, 10, 3, 11])
plt.plot( x2, g6,  "x", label = r'Messwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("5_s1.pdf")
plt.clf()


#Freier Fall Mittelwerte

MittelwerteFF = ([g7mittel, g8mittel, g9mittel])
StandardabweichungenMittelwerteFF = ([g7stanni, g8stanni, g9stanni])
#errX = ([ 0,0 ,0])
#errY = StandardabweichungenMittelwerteFF
xFF = np.linspace(0, 3, 3)
plt.axis([-1, 4, 3, 11])
#plt.plot( x3, Mittelwerte,  "x", label = r'Mittelwerte')
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.errorbar(xFF, MittelwerteFF, xerr = 0, yerr=StandardabweichungenMittelwerteFF, fmt = "x", label = r"Mittelwerte Freier Fall")
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("MittelwerteFF.pdf")
plt.clf()




#Schiefe Ebene Mittelwerte
MittelwerteSE = ([g1mittel, g2mittel, g3mittel, g4mittel, g5mittel, g6mittel])
StandardabweichungenMittelwerteSE = ([g1stanni, g2stanni, g3stanni, g4stanni, g5stanni, g6stanni])
errX = ([0, 0, 0, 0, 0, 0])
errY = StandardabweichungenMittelwerteSE
xSE = np.linspace(0, 6, 6)
plt.axis([-1, 7, 3, 11])
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.errorbar(xSE, MittelwerteSE, xerr = 0, yerr=StandardabweichungenMittelwerteSE, fmt = "x", label = r"Mittelwerte Schiefe Ebene")
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.xticks([])
plt.savefig("MittelwerteSE.pdf")
plt.clf()





#Alle Messungen (Mittelwerte)


Mittelwerte = ([g1mittel, g2mittel, g3mittel, g4mittel, g5mittel, g6mittel, g7mittel, g8mittel, g9mittel])
StandardabweichungenMittelwerte = ([g1stanni, g2stanni, g3stanni, g4stanni, g5stanni, g6stanni, g7stanni, g8stanni, g9stanni])
errX = ([0, 0, 0, 0, 0, 0, 0,0 ,0])
errY = StandardabweichungenMittelwerte
x3 = np.linspace(0, 9, 9)
plt.axis([-1, 10, 3, 11])
plt.plot( xg, g_plot, "-", label = r'Literaturwert')
plt.errorbar(x3, Mittelwerte, xerr = 0, yerr=StandardabweichungenMittelwerte, fmt = "x")
plt.ylabel(r"g [$m/s²$]")
plt.legend(loc = "best")
plt.savefig("Mittelwerte.pdf")
plt.xticks([])
plt.clf()
print(StandardabweichungenMittelwerte)

