import numpy as np
import matplotlib.pyplot as plt

x, D_0, D_a, D = np.genfromtxt("eeins.csv", delimiter=",", unpack = True)
l_e = 0.49
x_achs = l_e*x**2-x**3/3

params, covariance_matrix = np.polyfit(x_achs, D, deg = 1, cov = True)
x_plot = np.linspace(0, 0.08)

plt.plot(x_achs, D, "x", label =r"Messwerte")
plt.xlabel(r"3L²x-4x³")
plt.ylabel(r"D(x)")


plt.plot(x_plot, params[0] * x_plot + params[1], label = r'Lineare Regression')

plt.legend(loc = 'best')

plt.show()
plt.savefig("eeins.pdf")
plt.close()
print(params[0], params[1])