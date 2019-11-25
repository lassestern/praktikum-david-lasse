import numpy as np
import matplotlib.pyplot as plt

a, T = np.genfromtxt('I_Drill.txt', unpack = True)




plt.plot(a**2, T**2, 'x', label = r'Messwerte')
plt.xlabel(r'$a² [m²]$')
plt.ylabel(r'$T² [s²]$')



params, covariance_matrix = np.polyfit(a**2, T**2, deg = 1, cov = True)
x_plot = np.linspace(0, 0.1)
plt.plot(x_plot, params[0] * x_plot + params[1], label = r'Lineare Regression')

plt.legend(loc = 'best')
print(params[0], params[1])
errors = np.sqrt(np.diag(covariance_matrix))
print(errors)

plt.show()
plt.savefig('Drill.pdf')
plt.close()
