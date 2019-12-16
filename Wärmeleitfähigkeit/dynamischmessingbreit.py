import io
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

with io.open('GLXportRun2.txt', 'r', encoding = 'UTF-16') as f:
    Messung1, T1, T2, T3, T4, T5, T6, T7, T8, t = np.genfromtxt(f, unpack = True)


#Polyfit Untergund nah
Tf = 37.47, 41.66, 45.28, 48.32, 50.96, 53.25, 55.18
xf= 170, 250, 330, 412, 493, 573, 653
params, covariance_matrix = np.polyfit(xf, Tf, deg = 4, cov = True) 

#Polyfit Untergund nah
Tn = 38.28, 42.42, 46.64, 49.09, 51.73, 54.00, 55.96
xn = 163, 243, 323, 403, 484, 564, 644
param, cov_matrix = np.polyfit(xn, Tn, deg = 4, cov = True) 



#Polynom zum Untergrund fern
ff = params[0]*t**4 + params[1]*t**3 + params[2]*t**2 + params[3] * t + params[4]

#Polynom zum Untergrund nah
fn = param[0]*t**4 + param[1]*t**3 + param[2]*t**2 + param[3] * t + param[4]


#Messing breit
plt.plot(t, T1, "-", label =r"Messing breit fern")
plt.plot(t, T2, "-", label =r"Messing breit nah")
plt.plot(t, ff, "--", label =r"Untergrund fern")
plt.plot(t, fn, "--", label =r"Untergrund nah")
plt.xlabel(r"Zeit")
plt.ylabel(r"Temperatur")
plt.legend(loc = "best")
plt.show()
plt.savefig("dynamischmessingbreit.pdf")
plt.close
plt.clf()


#Messing dünn
plt.plot(t, T3, "-", label =r"Messing dünn nah")
plt.plot(t, T4, "-", label =r"Messing dünn fern")
plt.xlabel(r"Zeit")
plt.ylabel(r"Temperatur")
plt.legend(loc = "best")
plt.savefig("dynamischmessingdünn.pdf")
plt.clf()


#Gefilterte Funktionen
plt.plot(t, T1 - ff, "-")
plt.show()
plt.savefig("AmpMesbreitFern.pdf")
plt.close()
plt.clf()

plt.plot(t, T2 - fn, "-")
plt.show()
plt.savefig("AmpMesbreitNah.pdf")
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
def fern(t):
    return T1 - ff
maxima = find_peaks(fern(t), height = 0)
minima = find_peaks(-fern(t), height = -1)

#print(maxima)
#print(minima)

AMbf = ((2.52272909+ 2.53198607+ 2.51988986+ 2.55227662+ 2.60057457+2.62599013+ 2.66225868+ 2.62403024)/8 + (0.15891966+ 0.13057251+ 0.15738682+ 0.09272633+ 0.07717597+ 0.03407659+ 0.02228158+ 0.03941778)/8)/2

Maxmit_1 = (2.52272909+ 2.53198607+ 2.51988986+ 2.55227662+ 2.60057457+2.62599013+ 2.66225868+ 2.62403024)/8
Max_1 = [2.52272909, 2.53198607, 2.51988986, 2.55227662, 2.60057457, 2.62599013, 2.66225868, 2.62403024]
Maximafehler_1 = stanni(Max_1, Maxmit_1)

Minmit_1 = (0.15891966+ 0.13057251+ 0.15738682+ 0.09272633+ 0.07717597+ 0.03407659+ 0.02228158+ 0.03941778)/8
Min_1 = [0.15891966, 0.13057251, 0.15738682, 0.09272633, 0.07717597, 0.03407659, 0.02228158, 0.03941778]
Minimafehler_1 = stanni(Min_1, Minmit_1)


print('Fehler gemittelte Minima')
print(Minimafehler_1)
print('Fehler gemittelte Maxima')
print(Maximafehler_1)
print('Fehler gemittelte Amplitude')
print(abs(Minimafehler_1+Maximafehler_1))

print('gemittelte Amplitude Messing breit fern')
print(AMbf)

#Nah
def nah(t):
    return T2 - fn
maxima_n = find_peaks(nah(t), height = 0)
minima_n = find_peaks(-nah(t), height = -1)

#print(maxima_n)
#print(minima_n)

AMbn = ((9.29174973+ 9.45798862+ 9.21244194+ 9.05828167+ 9.02323589+ 9.15686035+ 9.33547991+ 9.3072003 + 8.92190807)/9 + (-0.04800006 -0.04884468+  0.22532431+  0.26851488+ 0.23177985+  0.04468475 -0.0949857)/7)/2

Maxmit = (9.29174973+ 9.45798862+ 9.21244194+ 9.05828167+ 9.02323589+ 9.15686035+ 9.33547991+ 9.3072003 + 8.92190807)/9
Max = [9.29174973, 9.45798862, 9.21244194, 9.05828167, 9.02323589, 9.15686035, 9.33547991, 9.3072003, 8.92190807]
Maximafehler = stanni(Max, Maxmit)

Minmit = (-0.04800006 -0.04884468+  0.22532431+  0.26851488+ 0.23177985+  0.04468475 -0.0949857)/7
Min = [-0.04800006, -0.04884468,  0.22532431,  0.26851488, 0.23177985,  0.04468475, -0.0949857]
Minimafehler = stanni(Min, Minmit)


print('Fehler gemittelte Minima')
print(Minimafehler)
print('Fehler gemittelte Maxima')
print(Maximafehler)
print('Fehler gemittelte Amplitude')
print(abs(Minimafehler+Maximafehler))

print('gemittelte Amplitude Messing breit nah')
print(AMbn)

#Bestimmung der Wärmeleitfähigkeit

k = 8520 * 385 * (0.03)**2 / (2 * 7.875 * np.log(9.3/2.7))

def kfehler(rho, c, x, t_m, A_n, A_f, A_ff, A_nf, t_mf ):
    return np.sqrt((rho * c * x**2 / (2* t_m * A_f * np.log(A_n / A_f)**2) * A_ff)**2 + 
                    (-rho * c * x**2 / (2* t_m * A_n * np.log(A_n / A_f)**2) * A_nf)**2 + 
                    (-rho * c * x**2 / (2* t_m**2 * np.log(A_n / A_f)) * t_mf)**2)

print('Wärmeleitfähigkeit Messing breit')
print(k)
print('Fehler von k')
print(kfehler(8520, 385, 0.03, 7.875, 9.3, 2.7, 0.3, 0.9, 0.5))

































































#with io.open('GLXportRun3.txt', 'r', encoding = 'UTF-16') as k:
    #Messung2, T11, T22, T33, T44, T55, T66, T77, T88, tt = np.genfromtxt(k, unpack = True)


#plt.plot(tt, T11, "-", label =r"T1")
#plt.plot(tt, T22, "-", label =r"T2")
#plt.plot(tt, T33, "-", label =r"T3")
#plt.plot(tt, T44, "-", label =r"T4")
#plt.xlabel(r"Zeit")
#plt.ylabel(r"Temperatur")
#plt.legend(loc = "best")
#plt.show()
#plt.savefig("dynamischmessing2.pdf")
#plt.close
#plt.clf()