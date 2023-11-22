import numpy as np

def sustreg(Ab, n):
    """
    Realiza la sustitución hacia atrás para una matriz triangular superior aumentada Ab,
    que proporciona la solución al sistema Ax = b. Aquí, A es de tamaño nxn y b es de tamaño nx1.

    Args:
    Ab: Matriz aumentada que representa el sistema Ax = b, con A en forma triangular superior.
    n: Número de filas (y columnas) de la matriz A.

    Returns:
    x: Vector solución del sistema.
    """

    x = np.zeros(n)  # Inicializa el vector solución con ceros.

    # Comienza la sustitución hacia atrás con el último elemento.
    x[n - 1] = Ab[n - 1, n] / Ab[n - 1, n - 1]

    # Itera hacia atrás desde la penúltima fila hasta la primera.
    for i in range(n - 2, -1, -1):
        suma = 0
        # Suma los productos de los coeficientes y las soluciones ya encontradas.
        for p in range(i + 1, n):
            suma += Ab[i, p] * x[p]
        # Calcula el valor de la variable actual.
        x[i] = (Ab[i, n] - suma) / Ab[i, i]

    return x
