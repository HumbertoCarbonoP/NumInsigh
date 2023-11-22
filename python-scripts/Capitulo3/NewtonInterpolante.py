import numpy as np
import matplotlib.pyplot as plt
import NewtonPolinomio

def NewtonInterpolante(x, y):
    """
    Calcula los coeficientes del polinomio de interpolación de Newton para un conjunto de puntos (x, y).

    Args:
    x: Lista o array de las coordenadas x de los puntos.
    y: Lista o array de las coordenadas y de los puntos.

    Returns:
    Tabla: Tabla de diferencias divididas de Newton.
    """

    n = len(x)  # Número de puntos.
    Tabla = np.zeros((n, n+1))  # Inicializa la tabla de diferencias divididas.
    Tabla[:, 0] = x  # Primer columna es x.
    Tabla[:, 1] = y  # Segunda columna es y.

    # Calcula la tabla de diferencias divididas.
    for j in range(2, n+1):
        for i in range(j-1, n):
            Tabla[i, j] = (Tabla[i, j-1] - Tabla[i-1, j-1]) / (Tabla[i, 0] - Tabla[i-j+2, 0])

    # Calcula el polinomio de interpolación de Newton (se asume la existencia de una función NewtonPolinomio).
    pol = NewtonPolinomio(x, np.diag(Tabla, 1))

    # Gráfica del polinomio interpolador y los puntos (comentado porque la implementación detallada no está incluida).
    xpol = np.linspace(x[0], x[-1], 1000)
    p = np.polyval(pol[::-1], xpol)
    plt.plot(x, y, 'r*', xpol, p, 'b-')
    plt.show()

    return Tabla

# Implementación de NewtonPolinomio y la gráfica estarían aquí.
