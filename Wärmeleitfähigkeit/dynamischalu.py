import io
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

with io.open('GLXportRun2.txt', 'r', encoding = 'UTF-16') as f:
    Messung1, T1, T2, T3, T4, T5, T6, T7, T8, t = np.genfromtxt(f, unpack = True)

#Polyfit Untergund nah
Tf = 35.14, 41.05, 45.20, 48.66, 51.47, 53.88, 55.99, 57.77
xf= 86, 166, 247, 327, 407, 487, 568, 648
params, covariance_matrix = np.polyfit(xf, Tf, deg = 4, cov = True) 

#Polyfit Untergund nah
Tn = 34.26, 39.94, 44.03, 47.49, 50.30, 52.75, 54.91, 56.72
xn = 81, 161, 242, 322, 402, 482, 562, 642
param, cov_matrix = np.polyfit(xn, Tn, deg = 4, cov = True) 



#Polynom zum Untergrund fern
ff = params[0]*t**4 + params[1]*t**3 + params[2]*t**2 + params[3] * t + params[4]

#Polynom zum Untergrund nah
fn = param[0]*t**4 + param[1]*t**3 + param[2]*t**2 + param[3] * t + param[4]

plt.plot(t, T5, "-", label =r"Alu dynamisch fern")
plt.plot(t, ff, "--", label =r"Untergrund fern")
plt.plot(t, T6, "-", label =r"Alu dynamisch nah")
plt.plot(t, fn, "--", label =r"Untergrund nah")
plt.xlabel(r"Zeit")
plt.ylabel(r"Temperatur")
plt.legend(loc = "best")
plt.show()
plt.savefig("dynamischalu1.pdf")
plt.close
plt.clf()


#Gefilterte Funktionen
plt.plot(t, T5 - ff, "-")
plt.show()
plt.savefig("AmpAluFern.pdf")
plt.close()
plt.clf()

plt.plot(t, T6 - fn, "-")
plt.show()
plt.savefig("AmpAluNah.pdf")
plt.close()
plt.clf()


#Amplituden bestimmen

#Formel für die Standardabweichung des Mittelwerts
def stanni(Zahlen, Mittelwert):
    i=0
    s=0
    n=len(Zahlen)
    while i<len(Zahlen):
        s = s + (Zahlen[i] - Mittelwert)**2
        i = i + 1
    return np.sqrt(s/(n*(n-1)))


#Fern
def fern(t):
    return T5 - ff
maxima = find_peaks(fern(t), height = 0)
minima = find_peaks(-fern(t), height = -1)

#print(maxima)
#print(minima)

Aaf = ((6.49724481+ 6.34566463+ 6.32110983+ 6.38303176 +6.30517506+ 6.30058292+ 6.24013388)/7 + (0.09288977+ 0.12234785+ 0.01638584+ 0.01421746)/4)/2

Maxmit_1 = (6.49724481+ 6.34566463+ 6.32110983+ 6.38303176 +6.30517506+ 6.30058292+ 6.24013388)/7
Max_1 = [6.49724481, 6.34566463, 6.32110983, 6.38303176, 6.30517506, 6.30058292, 6.24013388]
Maximafehler_1 = stanni(Max_1, Maxmit_1)
print('Maxmit fern')
print(Maxmit_1)

Minmit_1 = (0.09288977+ 0.12234785+ 0.01638584+ 0.01421746)/4
Min_1 = [0.09288977, 0.12234785, 0.01638584, 0.01421746]
Minimafehler_1 = stanni(Min_1, Minmit_1)
print('Minmit fern')
print(Minmit_1)

print('Fehler gemittelte Minima')
print(Minimafehler_1)
print('Fehler gemittelte Maxima')
print(Maximafehler_1)
print('Fehler gemittelte Amplitude')
print(abs(Minimafehler_1+Maximafehler_1))

print('gemittelte Amplitude Alu fern')
print(Aaf)

#Nah
def nah(t):
    return T6 - fn
maxima_n = find_peaks(nah(t), height = 0)
minima_n = find_peaks(-nah(t), height = -1)

#print(maxima_n)
#print(minima_n)

Aan = ((13.0378683+13.38081272+13.20834859+13.21141298+13.21200414+13.11318156+13.05906596+12.94483923+13.12674451)/9 + (1.00200682*10**(-1) -2.56136577*10**(-2) + 9.73946728*10**(-2) - 2.72419893*10**(-2) - 2.70525218*10**(-2) - 6.27017413*10**(-4) + 4.75024020*10**(-2))/7)/2


Maxmit = (13.0378683+13.38081272+13.20834859+13.21141298+13.21200414+13.11318156+13.05906596+12.94483923+13.12674451)/9
Max = [13.0378683, 13.38081272, 13.20834859, 13.21141298, 13.21200414, 13.11318156, 13.05906596, 12.94483923, 13.12674451]
Maximafehler = stanni(Max, Maxmit)
print('Maxmit nah')
print(Maxmit)

Minmit = (1.00200682*10**(-1) -2.56136577*10**(-2) + 9.73946728*10**(-2) - 2.72419893*10**(-2) - 2.70525218*10**(-2) - 6.27017413*10**(-4) + 4.75024020*10**(-2))/7
Min = [1.00200682*10**(-1),  -2.56136577*10**(-2), + 9.73946728*10**(-2), - 2.72419893*10**(-2), - 2.70525218*10**(-2), - 6.27017413*10**(-4), + 4.75024020*10**(-2)]
Minimafehler = stanni(Min, Minmit)
print('Minmit nah')
print(Minmit)


print('Fehler gemittelte Minima')
print(Minimafehler)
print('Fehler gemittelte Maxima')
print(Maximafehler)
print('Fehler gemittelte Amplitude')
print(abs(Minimafehler+Maximafehler))

print('gemittelte Amplitude Alu nah')
print(Aan)
#Bestimmung der Wärmeleitfähigkeit

k = 2800 * 830 * (0.03)**2 / (2 * 5.25 * np.log(13.2/6.4))

def kfehler(rho, c, x, t_m, A_n, A_f, A_ff, A_nf, t_mf ):
    return np.sqrt((rho * c * x**2 / (2* t_m * A_f * np.log(A_n / A_f)**2) * A_ff)**2 + 
                    (-rho * c * x**2 / (2* t_m * A_n * np.log(A_n / A_f)**2) * A_nf)**2 + 
                    (-rho * c * x**2 / (2* t_m**2 * np.log(A_n / A_f)) * t_mf)**2)

print('Wärmeleitfähigkeit Alu')
print(k)
print('Fehler k')
print(kfehler(2800, 830, 0.03, 5.25, 13.2, 6.4, 0.3, 0.6, 0.2))












#with io.open('GLXportRun3.txt', 'r', encoding = 'UTF-16') as k:
#    Messung2, T11, T22, T33, T44, T55, T66, T77, T88, tt = np.genfromtxt(k, unpack = True)
#
#
#plt.plot(tt, T55, "-", label =r"Alu dynamisch fern")
#plt.plot(tt, T66, "-", label =r"Alu dynamisch nah")
#plt.xlabel(r"Zeit")
#plt.ylabel(r"Temperatur")
#plt.legend(loc = "best")
#plt.show()
#plt.savefig("dynamischalu2.pdf")
#plt.close
#plt.clf()