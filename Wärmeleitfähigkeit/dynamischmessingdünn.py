import io
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

with io.open('GLXportRun2.txt', 'r', encoding = 'UTF-16') as f:
    Messung1, T1, T2, T3, T4, T5, T6, T7, T8, t = np.genfromtxt(f, unpack = True)


#Polyfit Untergund fern
Tf = 32.53, 37.24, 40.88, 43.98, 46.58, 48.82, 50.74, 52.44 
xf= 89, 170, 251, 331, 411, 492, 573, 653
params, covariance_matrix = np.polyfit(xf, Tf, deg = 4, cov = True) 

#Polyfit Untergund nah
Tn = 33.24, 38.00, 41.67, 44.9, 47.58, 49.93, 51.95, 53.69
xn = 83, 163, 243, 323, 403, 483, 564, 644
param, cov_matrix = np.polyfit(xn, Tn, deg = 4, cov = True) 



#Polynom zum Untergrund fern
ff = params[0]*t**4 + params[1]*t**3 + params[2]*t**2 + params[3] * t + params[4]

#Polynom zum Untergrund nah
fn = param[0]*t**4 + param[1]*t**3 + param[2]*t**2 + param[3] * t + param[4]


#Messing breit
#plt.plot(t, T1, "-", label =r"Messing breit fern")
#plt.plot(t, T2, "-", label =r"Messing breit nah")
#plt.plot(t, ff, "--", label =r"Untergrund fern")
#plt.plot(t, fn, "--", label =r"Untergrund nah")
#plt.xlabel(r"Zeit")
#plt.ylabel(r"Temperatur")
#plt.legend(loc = "best")
#plt.show()
#plt.savefig("dynamischmessingbreit.pdf")
#plt.close
#plt.clf()


#Messing dünn
plt.plot(t, T3, "-", label =r"Messing dünn nah")
plt.plot(t, T4, "-", label =r"Messing dünn fern")
plt.plot(t, ff, "--", label =r"Untergrund fern")
plt.plot(t, fn, "--", label =r"Untergrund nah")
plt.xlabel(r"Zeit")
plt.ylabel(r"Temperatur")
plt.legend(loc = "best")
plt.savefig("dynamischmessingdünn.pdf")
plt.clf()


#Gefilterte Funktionen
plt.plot(t, T4 - ff, "-")
plt.show()
plt.savefig("AmpMesdünnFern.pdf")
plt.close()
plt.clf()

plt.plot(t, T3 - fn, "-")
plt.show()
plt.savefig("AmpMesdünnNah.pdf")
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
    return T4 - ff
maxima = find_peaks(fern(t), height = 0)
minima = find_peaks(-fern(t), height = -1)

#print(maxima)
#print(minima)

AMdf = (3.07097907+ 3.05059809+ 3.05241335+ 3.06536042+ 3.09011985+ 3.09834598+ 3.05403914)/7 + (0.18179033+ 0.05394461+ 0.1091292 + 0.06507233+ 0.04517959+ 0.01853387+ 0.04235412+ 0.0086013)/8

Maxmit_1 = (3.07097907+ 3.05059809+ 3.05241335+ 3.06536042+ 3.09011985+ 3.09834598+ 3.05403914)/7
Max_1 = [3.07097907, 3.05059809, 3.05241335, 3.06536042, 3.09011985, 3.09834598, 3.05403914]
Maximafehler_1 = stanni(Max_1, Maxmit_1)

Minmit_1 = (0.18179033+ 0.05394461+ 0.1091292 + 0.06507233+ 0.04517959+ 0.01853387+ 0.04235412+ 0.0086013)/8
Min_1 = [0.18179033, 0.05394461, 0.1091292, 0.06507233, 0.04517959, 0.01853387, 0.04235412, 0.0086013]
Minimafehler_1 = stanni(Min_1, Minmit_1)


print('Fehler gemittelte Minima')
print(Minimafehler_1)
print('Fehler gemittelte Maxima')
print(Maximafehler_1)
print('Fehler gemittelte Amplitude')
print(abs(Minimafehler_1+Maximafehler_1))

print('gemittelte Amplitude Messing dünn fern')
print(AMdf)

#Nah
def nah(t):
    return T3 - fn
maxima_n = find_peaks(nah(t), height = 0)
minima_n = find_peaks(-nah(t), height = -1)

#print(maxima_n)
#print(minima_n)

AMdn = (11.07928284+ 11.14849644+ 10.99394061+ 10.99313695+ 10.9349915 +10.92979469+ 10.88372595+ 10.79494066+ 10.94953921)/9 + ( 0.01420754 -0.05414268+ 0.06643879 -0.01726187 -0.00859519 -0.01728698+  0.0265831  -0.008695)/8

Maxmit = (11.07928284+ 11.14849644+ 10.99394061+ 10.99313695+ 10.9349915 +10.92979469+ 10.88372595+ 10.79494066+ 10.94953921)/9
Max = [11.07928284, 11.14849644, 10.99394061, 10.99313695, 10.9349915, 10.92979469, 10.88372595, 10.79494066, 10.94953921]
Maximafehler = stanni(Max, Maxmit)

Minmit = ( 0.01420754 -0.05414268+ 0.06643879 -0.01726187 -0.00859519 -0.01728698+  0.0265831  -0.008695)/8
Min = [0.01420754, -0.05414268, 0.06643879, -0.01726187, -0.00859519, -0.01728698,  0.0265831,  -0.008695]
Minimafehler = stanni(Min, Minmit)


print('Fehler gemittelte Minima')
print(Minimafehler)
print('Fehler gemittelte Maxima')
print(Maximafehler)
print('Fehler gemittelte Amplitude')
print(abs(Minimafehler+Maximafehler))

print('gemittelte Amplitude Messing dünn nah')
print(AMdn)


#Bestimmung der Wärmeleitfähigkeit

k = 8520 * 385 * (0.03)**2 / (2 * 8 * np.log(11/3.1))

def kfehler(rho, c, x, t_m, A_n, A_f, A_ff, A_nf, t_mf ):
    return np.sqrt((rho * c * x**2 / (2* t_m * A_f * np.log(A_n / A_f)**2) * A_ff)**2 + 
                    (-rho * c * x**2 / (2* t_m * A_n * np.log(A_n / A_f)**2) * A_nf)**2 + 
                    (-rho * c * x**2 / (2* t_m**2 * np.log(A_n / A_f)) * t_mf)**2)

print('Wärmeleitfähigkeit Messing dünn')
print(k)
print('k Fehler')
print(kfehler(8520, 385, 0.03, 8, 11.0, 3.1, 0.2, 0.4, 0.4))