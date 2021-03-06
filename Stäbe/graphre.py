import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt

x, D_0, D_a, D = np.genfromtxt("rein.csv", delimiter=",", unpack = True)
l_e = 0.49
x_achs = l_e*x**2-x**3/3


plt.plot(x_achs, D*10**(-3), "x", label =r"Messwerte")
plt.xlabel(r"Lx²-x³/3 [m³]")
plt.ylabel(r"D(x) [m]")

params, covariance_matrix = np.polyfit(x_achs, D*10**(-3), deg = 1, cov = True)
x_plot = np.linspace(0, 0.08)

plt.plot(x_plot, params[0] * x_plot + params[1], label = r'Lineare Regression')

plt.legend(loc = 'best')

plt.show()
plt.savefig("reins.pdf")
plt.close()
errors = np.sqrt(np.diag(covariance_matrix[0]))

I=np.pi*0.0044**4/4

E=(0.0207+0.0189+1.1686)*const.g /(2*I*params[0])
delta_e =(0.0207+0.0189+1.1686)*const.g /(2*I*params[0]**2) * errors[0]

print("Elastizitätsmodul")
print(E)
print(errors)
print(delta_e)
#print(params)