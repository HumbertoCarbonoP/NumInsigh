import numpy as np
import matplotlib.pyplot as plt

# Datos iniciales.
x = np.array([0, 1, 2, 3])
y = np.array([-0.1, 0.2, 0.5, 0.8])

# Creación de la matriz de diseño A para un polinomio cúbico.
A = np.column_stack((x**3, x**2, x, np.ones_like(x)))
b = y

# Cálculo de los coeficientes del polinomio.
a = np.linalg.inv(A) @ b

# Creación de puntos para el trazado del polinomio.
xpol = np.linspace(x[0], x[-1], 1000)
p = a[0]*xpol**3 + a[1]*xpol**2 + a[2]*xpol + a[3]

# Trazado de los puntos y el polinomio.
plt.plot(x, y, 'r*', label='Puntos originales')
plt.plot(xpol, p, 'b-', label='Polinomio interpolador')
plt.grid(True)
plt.legend()

# Cálculo e inclusión de un punto interpolado.
p0 = a[0]*1.5**3 + a[1]*1.5**2 + a[2]*1.5 + a[3]
plt.plot(1.5, p0, 'g*', label='Interpolación en x=1.5')
plt.legend()

plt.show()
