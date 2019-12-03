import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

x, D_0, D_a, D = np.genfromtxt("eeins.csv", delimiter=",", unpack = True)
l_e = 0.49
x_achs = l_e*x**2-x**3/3

params, covariance_matrix = np.polyfit(x_achs, D*10**(-3), deg = 1, cov = True)
x_plot = np.linspace(0, 0.08)

plt.plot(x_achs, D*10**(-3), "x", label =r"Messwerte")
plt.xlabel(r"Lx²-x³/3 [m³]")
plt.ylabel(r"D(x) [m]")


plt.plot(x_plot, params[0] * x_plot + params[1], label = r'Lineare Regression')

plt.legend(loc = 'best')

plt.show()
plt.savefig("eeins.pdf")
plt.close()
print(params[0], params[1])

I=0.0122*0.0110**3/12

errors = np.sqrt(np.diag(covariance_matrix[0]))

E=((0.0207+0.0189+1.1686+1.1597)*const.g) /(2*I*params[0])
delta_e=((0.0207+0.0189+1.1686+1.1597)*const.g) /(2*I*params[0]**2) * errors
print(E)
print(errors)
print(delta_e)
#print(params)
