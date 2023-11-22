import numpy as np

def directLU(A, met):
    """
    Calcula la factorización LU de la matriz A.

    Args:
    A: Matriz a factorizar.
    met: Método de factorización (0 para Doolittle, 1 para Crout, 2 para Cholesky).

    Returns:
    L: Matriz triangular inferior.
    U: Matriz triangular superior.
    """

    n = len(A)
    U = np.eye(n)  # Inicializa U como matriz identidad.
    L = np.copy(U)  # Inicializa L como matriz identidad.

    for k in range(n):
        sum1 = sum(L[k, p] * U[p, k] for p in range(k))

        if met == 0:  # Método de Doolittle.
            U[k, k] = (A[k, k] - sum1) / L[k, k]
        elif met == 1:  # Método de Crout.
            L[k, k] = (A[k, k] - sum1) / U[k, k]
        else:  # Método de Cholesky.
            U[k, k] = np.sqrt(A[k, k] - sum1)
            L[k, k] = U[k, k]

        for i in range(k + 1, n):
            sum2 = sum(L[i, p] * U[p, k] for p in range(k))
            L[i, k] = (A[i, k] - sum2) / U[k, k]

        for j in range(k + 1, n):
            sum3 = sum(L[k, p] * U[p, j] for p in range(k))
            U[k, j] = (A[k, j] - sum3) / L[k, k]

    return L, U
