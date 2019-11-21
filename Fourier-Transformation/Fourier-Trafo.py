import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

FT = 17

#f(x)=x
#w_1=k #Frequenz von x
T_1 = 2*np.pi #Periodendauer von x

Bk = []
Bk.append(0) #Bk(k=0)=0
k = 1
while k<=FT:
    f = lambda x: (2/T_1) * x * np.sin(x*k)
    B = integrate.quad(f, -np.pi, np.pi)
    Bk.append(B[0]) #B sieht so aus: (bk, anderer Wert). Wir wollen bk also B[0]
    k += 1

print(Bk)    

j = 0
func = 0
x1 = np.linspace(-np.pi, np.pi,1000)

while j <= FT:
    func += Bk[j] * np.sin(j*x1)
    j += 1

print(func)
y1=x1 #Funktion f(x)=x drübergelegt

plt.plot(x1, y1, label = 'f(t)=t')
plt.plot(x1, func, label = 'Fouriersynthese')
plt.xlim(-np.pi - 0.5, np.pi + 0.5)
plt.ylim(-5, 5)
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc = 'best')
plt.savefig('plot_x.pdf')

plt.show()


#f(x)=|sin(x)|
#w_2=2*q #Frequenz von |sin(x)|
T_2=np.pi #Periodendauer von |sin(x)|
Ak = []

p = lambda c: 1/T_2 * np.abs(np.sin(c))
A_0, err = integrate.quad(p, -np.pi /2, np.pi /2) 
Ak.append(A_0)

q=1
while q<=FT:
     P = lambda v: (2/T_2) * np.abs(np.sin(v)) * np.cos(q*2*v)
     A = integrate.quad(P, -np.pi /2, np.pi /2)
     Ak.append(A[0])
     q += 1

print(Ak)

i = 0
func2 = 0
x2=np.linspace(-np.pi,np.pi,1000)
while i <= FT:
    func2+=(Ak[i] * np.cos(2*i*x2))
    i += 1

finalfunc = np.sum(func)
y2=np.abs(np.sin(x2)) #Funktion f(x)=|sin(x)| drübergelegt

plt.figure(figsize=(10,4))
plt.plot(x2, y2, label = r"$f(t)=|sin(t)|$")
plt.plot(x2, func2, label = "Fouriersynthese")
plt.xlim(-np.pi - 0.5, np.pi + 0.5)
plt.xticks([-np.pi, -(np.pi/2), 0, np.pi/2, np.pi],[r"$-\pi$", r'$-\pi/2$', "$0$", r'$\pi/2$', r"$\pi$"])
plt.xlabel(r'$t$')
plt.ylabel(r'$f(t)$')
plt.legend(loc = "best")
plt.savefig('plot_sin.pdf')

plt.show()