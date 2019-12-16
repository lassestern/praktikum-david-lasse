import io
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

with io.open('GLXportRun3.txt', 'r', encoding = 'UTF-16') as k:
    Messung2, T11, T22, T33, T44, T55, T66, T77, T88, tt = np.genfromtxt(k, unpack = True)

#Polyfit Untergund fern
Tf = 34.19, 38.75, 42.36, 45.08, 47.42
xf= 228, 436, 641, 845, 1048
params, covariance_matrix = np.polyfit(xf, Tf, deg = 3, cov = True) 

#Polyfit Untergund nah
Tn = 39.66, 44.68, 48.38, 51.05, 53.40
xn = 207, 408, 609, 809, 1010
param, cov_matrix = np.polyfit(xn, Tn, deg = 3, cov = True) 



#Polynom zum Untergrund fern
ff = params[0]*tt**3 + params[1]*tt**2 + params[2]*tt + params[3] 

#Polynom zum Untergrund nah
fn = param[0]*tt**3 + param[1]*tt**2 + param[2]*tt + param[3]



#plt.plot(t, T8, "-", label =r"Edelstahl dynamisch fern")
#plt.plot(t, T7, "-", label =r"Edelstahl dynamisch nah")
#plt.xlabel(r"Zeit")
#plt.ylabel(r"Temperatur")
#plt.legend(loc = "best")
#plt.show()
#plt.savefig("dynamischstahl1.pdf")
#plt.close
#plt.clf()




plt.plot(tt, T88, "-", label =r"Edelstahl dynamisch fern")
plt.plot(tt, T77, "-", label =r"Edelstahl dynamisch nah")
plt.plot(tt, ff, "--", label =r"Untergrund fern")
plt.plot(tt, fn, "--", label =r"Untergrund nah")
plt.xlabel(r"Zeit")
plt.ylabel(r"Temperatur")
plt.legend(loc = "best")
plt.show()
plt.savefig("dynamischstahl2.pdf")
plt.close
plt.clf()

#Gefilterte Funktionen
plt.plot(tt, T88 - ff, "-")
plt.show()
plt.savefig("AmpStahlFern.pdf")
plt.close()
plt.clf()

plt.plot(tt, T77 - fn, "-")
plt.show()
plt.savefig("AmpStahlNah.pdf")
plt.close()
plt.clf()


#Amplituden bestimmen

#Formel für die Standardabweichung des Mittelwerts
def stanni(Zahlen, Mittelwert):
    i=0
    s=0
    while i<len(Zahlen):
        s = s + (Zahlen[i] - Mittelwert)**2
        i = i + 1
    return np.sqrt(s)

#Fern
def fern(tt):
    return T88 - ff
maxima = find_peaks(fern(tt), height = 0)
minima = find_peaks(-fern(tt), height = -1)

#print(maxima)
#print(minima)

ASf = (1.72031989+1.71229188+1.78683186)/3 + (0.03916327+0.10622593+0.10354813)/3

Maxmit_1 = (1.72031989+1.71229188+1.78683186)/3
Max_1 = [1.72031989, 1.71229188, 1.78683186]
Maximafehler_1 = stanni(Max_1, Maxmit_1)

Minmit_1 = (0.03916327+0.10622593+0.10354813)/3
Min_1 = [0.03916327, 0.10622593, 0.10354813]
Minimafehler_1 = stanni(Min_1, Minmit_1)


print('Fehler gemittelte Minima')
print(Minimafehler_1)
print('Fehler gemittelte Maxima')
print(Maximafehler_1)
print('Fehler gemittelte Amplitude')
print(abs(Minimafehler_1+Maximafehler_1))

print('gemittelte Amplitude Stahl fern')
print(ASf)

#Nah
def nah(tt):
    return T77 - fn
maxima_n = find_peaks(nah(tt), height = 0)
minima_n = find_peaks(-nah(tt), height = -1)

#print(maxima_n)
#print(minima_n)

ASn = (14.47301367+ 14.41325395+ 14.392095  + 14.28839464+ 14.38114018)/5 + (0.03329483+ 0.03299853 -0.02735525+  0.02409037 -0.00545716)/5

Maxmit = (14.47301367+ 14.41325395+ 14.392095  + 14.28839464+ 14.38114018)/5
Max = [14.47301367, 14.41325395, 14.392095, 14.28839464, 14.38114018]
Maximafehler = stanni(Max, Maxmit)

Minmit = (0.03329483+ 0.03299853 -0.02735525+  0.02409037 -0.00545716)/5 
Min = [0.03329483, 0.03299853, -0.02735525,  0.02409037, -0.00545716]
Minimafehler = stanni(Min, Minmit)


print('Fehler gemittelte Minima')
print(Minimafehler)
print('Fehler gemittelte Maxima')
print(Maximafehler)
print('Fehler gemittelte Amplitude')
print(abs(Minimafehler+Maximafehler))

print('gemittelte Amplitude Stahl nah')
print(ASn)


#Bestimmung der Wärmeleitfähigkeit

k = 8000 * 400 * (0.03)**2 / (2 * 31 * np.log(14.40/1.82))

def kfehler(rho, c, x, t_m, A_n, A_f, A_ff, A_nf, t_mf ):
    return np.sqrt((rho * c * x**2 / (2* t_m * A_f * np.log(A_n / A_f)**2) * A_ff)**2 + 
                    (-rho * c * x**2 / (2* t_m * A_n * np.log(A_n / A_f)**2) * A_nf)**2 + 
                    (-rho * c * x**2 / (2* t_m**2 * np.log(A_n / A_f)) * t_mf)**2)

print('Wärmeleitfähigkeit Stahl')
print(k)
print('Fehler k')
print(kfehler(8000, 400, 0.03, 31, 14.40, 1.82, 0.12, 0.19, 3.04))