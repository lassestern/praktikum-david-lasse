import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as const

irrel, D_0, D_a, D, x = np.genfromtxt("ezwei.csv", delimiter=",", unpack = True)
x_reg1, D_reg1 = np.genfromtxt("ezuhr1.csv", delimiter=",", unpack = True)
x_reg2, D_reg2 = np.genfromtxt("ezuhr2.csv", delimiter=",", unpack = True)
l_e = 0.55
x_achs = x*3*l_e**2-4*x**3
x_reg1a = 3*l_e**2*x_reg1-4*x_reg1**3
x_reg2a = 3*l_e**2*x_reg2-4*x_reg2**3



plt.plot(x_achs, D*10**(-3), "x", label =r"Graph Eckig zweiseitig")
plt.xlabel(r"3L²x-4x³ [m³]")
plt.ylabel(r"D(x) [m]")

params_1, covariance_matrix_1 = np.polyfit(x_reg1a, D_reg1*10**(-3), deg = 1, cov = True)
x_plot = np.linspace(0, 0.17)

plt.plot(x_plot, params_1[0] * x_plot + params_1[1], label = r'Lineare Regression Uhr 1')



params_2, covariance_matrix_2 = np.polyfit(x_reg2a, D_reg2*10**(-3), deg = 1, cov = True)

plt.plot(x_plot, params_2[0] * x_plot + params_2[1], label = r'Lineare Regression Uhr 2')

plt.legend(loc = 'best')

plt.show()
plt.savefig("ezwei.pdf")
plt.close()

I=0.0122**3*0.0110/12

a_D = (params_1[0]+params_2[0])/2

E=(0.0207+0.0189+1.1686+1.1597)*const.g /(48*I*a_D)
E_1=(0.0207+0.0189+1.1686+1.1597)*const.g /(48*I*params_1[0])
E_2=(0.0207+0.0189+1.1686+1.1597)*const.g /(48*I*params_2[0])

errors_1 = np.sqrt(np.diag(covariance_matrix_1[0]))
errors_2 = np.sqrt(np.diag(covariance_matrix_2[0]))
delta_e= (0.0207+0.0189+1.1686+1.1597)*const.g /(48*I*a_D**2) * ((errors_1[0]+errors_2[0])/2)

print('Elastizitätsmodul im Durchschnitt')
print(E)
print('Elastizitätsmodul von Uhr 1')
print(E_1)
print('Elastizitätsmodul von Uhr 2')
print(E_2)
print('Fehler von Uhr 1')
print(errors_1)
print('Fehler von Uhr 2')
print(errors_2)
print('Gemittelter Fehler')
print(delta_e)
print(params_1, params_2)