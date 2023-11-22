import numpy as np

def Lagrange(x, y):
    """
    Calcula los coeficientes del polinomio de interpolación de Lagrange para un conjunto de puntos (x, y).

    Args:
    x: Lista o array de las coordenadas x de los puntos.
    y: Lista o array de las coordenadas y de los puntos.

    Returns:
    pol: Coeficientes del polinomio interpolador.
    """

    n = len(x)  # Número de puntos.
    Tabla = np.zeros((n, n))  # Inicializa una tabla para almacenar los polinomios Li.

    for i in range(n):
        Li = np.array([1])  # Inicializa el polinomio Li como 1.
        den = 1  # Denominador para normalizar Li.

        for j in range(n):
            if j != i:
                paux = np.array([1, -x[j]])  # Polinomio auxiliar (x - x[j]).
                Li = np.polymul(Li, paux)  # Multiplica Li por el polinomio auxiliar.
                den *= (x[i] - x[j])  # Actualiza el denominador.

        Tabla[i, :] = y[i] * Li / den  # Escala Li y lo almacena en la tabla.

    pol = np.sum(Tabla, axis=0)  # Suma los polinomios Li para obtener el polinomio interpolador.

    return pol
