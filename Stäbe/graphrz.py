import numpy as np
import matplotlib.pyplot as plt

irrel, D_0, D_a, D, x, x_reg1, x_reg2, D_reg1, D_reg2 = np.genfromtxt("rzwei.csv", delimiter=",", unpack = True)
l_e = 0.55
x_achs = l_e*x**2-x**3/3


plt.plot(x_achs, D, "x", label =r"Graph Rund zweiseitig")
plt.xlabel(r"3L²x-4x³")
plt.ylabel(r"D(x)")

x_reg1a = l_e*x_reg1**2-x_reg1**3/3
x_reg2a = l_e*x_reg2**2-x_reg2**3/3



plt.plot(x_achs, D, "x", label =r"Graph Eckig zweiseitig")
plt.xlabel(r"3L²x-4x³")
plt.ylabel(r"D(x)")

params_1, covariance_matrix_1 = np.polyfit(x_reg1a, D_reg1, deg = 1, cov = True)
x_plot = np.linspace(0, 0.03)

plt.plot(x_plot, params_1[0] * x_plot + params_1[1], label = r'Lineare Regression Uhr 1')



params_2, covariance_matrix_2 = np.polyfit(x_reg2a, D_reg2, deg = 1, cov = True)

plt.plot(x_plot, params_2[0] * x_plot + params_2[1], label = r'Lineare Regression Uhr 2')

plt.legend(loc = 'best')

plt.show()
plt.savefig("rzwei.pdf")
plt.close()