import numpy as np

def NewtonPolinomio(x, coef):
    """
    Calcula los coeficientes del polinomio interpolador de Newton.

    Args:
    x: Lista o array de las coordenadas x de los puntos.
    coef: Coeficientes de la tabla de diferencias divididas de Newton.

    Returns:
    pol: Coeficientes del polinomio interpolador de Newton.
    """

    n = len(x)  # Número de puntos.
    acum = np.array([1])  # Acumulador inicializado a 1.
    pol = coef[0] * acum  # Inicializa el polinomio con el primer coeficiente.

    for i in range(n - 1):
        pol = np.pad(pol, (1, 0))  # Agrega un cero al inicio del polinomio.
        acum = np.polymul(acum, np.array([1, -x[i]]))  # Multiplica acum por (x - x[i]).
        pol = pol + coef[i + 1] * acum  # Agrega el siguiente término al polinomio.

    return pol
