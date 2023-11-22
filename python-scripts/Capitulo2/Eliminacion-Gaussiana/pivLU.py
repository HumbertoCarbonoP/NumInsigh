def pivLU(A, P, n, k):
    """
    Realiza el pivoteo parcial sobre la matriz A para la factorización LU en el contexto del sistema Ax = b.

    Args:
    A: Matriz de coeficientes del sistema.
    P: Matriz de permutación actual.
    n: Número total de filas en la matriz A.
    k: Índice actual para el pivoteo.

    Returns:
    A: Matriz de coeficientes actualizada después del pivoteo.
    P: Matriz de permutación actualizada.
    """

    mayor = abs(A[k, k])  # Valor absoluto del elemento actual.
    maxrow = k  # Índice de la fila con el mayor valor absoluto en la columna k.

    # Busca el mayor valor absoluto en la columna actual, empezando por la fila k.
    for s in range(k + 1, n):
        if abs(A[s, k]) > mayor:
            mayor = abs(A[s, k])
            maxrow = s

    # Verifica si el mayor valor encontrado es cero.
    if mayor == 0:
        print('El sistema no tiene solución única')
    # Realiza el intercambio de filas en A y P si se encuentra una fila con un valor mayor.
    elif maxrow != k:
        A[[k, maxrow]] = A[[maxrow, k]]
        P[[k, maxrow]] = P[[maxrow, k]]

    return A, P
