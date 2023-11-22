import numpy as np

def sustpro(Ab, n):
    """
    Realiza la sustitución hacia adelante para una matriz triangular inferior aumentada Ab,
    que proporciona la solución al sistema Ax = b. Aquí, A es de tamaño nxn y b es de tamaño nx1.

    Args:
    Ab: Matriz aumentada que representa el sistema Ax = b, con A en forma triangular inferior.
    n: Número de filas (y columnas) de la matriz A.

    Returns:
    x: Vector solución del sistema.
    """

    x = np.zeros(n)  # Inicializa el vector solución con ceros.

    # Comienza la sustitución hacia adelante con el primer elemento.
    x[0] = Ab[0, n] / Ab[0, 0]

    # Itera desde la segunda fila hasta la última.
    for i in range(1, n):
        suma = 0
        # Suma los productos de los coeficientes conocidos y sus soluciones calculadas previamente.
        for p in range(i):
            suma += Ab[i, p] * x[p]
        # Calcula el valor de la variable actual.
        x[i] = (Ab[i, n] - suma) / Ab[i, i]

    return x
