import numpy as np
import matplotlib.pyplot as plt

x, F = np.genfromtxt('werte.txt', unpack=True)
plt.plot(x, F, 'x', label = r'Messwerte')
plt.xlabel(r'$\Delta x \ [cm]$')
plt.ylabel(r'$F \ [N]$')

params, covariance_matrix = np.polyfit(x, F, deg = 1, cov = True)
x_plot = np.linspace(0, 50)
plt.plot(x_plot, params[0] * x_plot + params[1], label = r'Lineare Regression')

plt.legend(loc = 'best')

plt.savefig('Hookgraph.pdf')

plt.show()

print(params[0], params[1])