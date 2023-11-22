import numpy as np
import sustpro
import sustreg
import pivLU

def LU(A, b, n, Piv):
    """
    Calcula la solución de un sistema de ecuaciones Ax = b usando la factorización LU de A.
    Puede realizar la factorización con o sin pivoteo parcial.

    Args:
    A: Matriz de coeficientes del sistema.
    b: Vector de términos constantes.
    n: Tamaño de la matriz A (nxn).
    Piv: Indica si se usa pivoteo parcial (1) o no (0).

    Returns:
    x: Vector solución del sistema.
    L: Matriz triangular inferior de la factorización LU.
    U: Matriz triangular superior de la factorización LU.
    P: Matriz de permutación resultante del pivoteo.
    """

    P = np.eye(n)  # Matriz de permutación inicializada como matriz identidad.
    L = np.copy(P)  # L inicializada como matriz identidad.

    # Factorización LU con o sin pivoteo parcial.
    for k in range(n - 1):
        if Piv == 1:
            A, P = pivLU(A, P, n, k)  # Función de pivoteo (no implementada aquí).

        for i in range(k + 1, n):
            M = A[i, k] / A[k, k]
            A[i, k:n] -= M * A[k, k:n]
            A[i, k] = M

    U = np.triu(A)  # U es la parte triangular superior de A.
    L += np.tril(A, -1)  # L es la suma de la identidad y la parte triangular inferior de A.

    # Resolviendo Ly = b con el método de sustitución hacia adelante.
    B = np.dot(P, b)
    LB = np.hstack([L, B.reshape(-1, 1)])
    z = sustpro(LB, n)  # Función de sustitución hacia adelante (no implementada aquí).

    # Resolviendo Ux = z con el método de sustitución hacia atrás.
    Uz = np.hstack([U, z.reshape(-1, 1)])
    x = sustreg(Uz, n)  # Función de sustitución hacia atrás (no implementada aquí).

    return x, L, U, P
