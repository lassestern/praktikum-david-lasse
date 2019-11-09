import numpy as np
from scipy import integrate 

FT=17
k=1


#f(x)=x
w_1=k
T_1=2*np.pi

Bk = []
Bk.append(0) #Bk(k=0)=0
while k<=FT:
    f = lambda x: (2/T_1)*x*np.sin(x*k)
    B = integrate.quad(f, -np.pi, np.pi)
    Bk.append(B[0]) #B sieht so aus: (bk, anderer Wert). Wir wollen bk also B[0]
    k += 1

print(Bk)    


q=1

#f(x)=|sin(x)|
w_2=2*q
T_2=np.pi
Ak = []
p = lambda c: 1/T_2 * np.abs(np.sin(c))

A_0 = integrate.quad(p, -np.pi /2, np.pi /2) 
Ak.append(A_0[0])

while q<=FT:
     P = lambda v: (2/T_2) * np.abs(np.sin(v)) * np.cos(q*2*v)
     A = integrate.quad(P, -np.pi /2, np.pi /2)
     Ak.append(A[0])
     q += 1

print(Ak)