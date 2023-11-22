def pivpar(Ab, n, k):
    """
    Realiza el pivoteo parcial sobre la matriz aumentada Ab del sistema Ax = b.

    Args:
    Ab: Matriz aumentada del sistema Ax = b.
    n: Número total de filas en la matriz Ab.
    k: Índice de la columna actual para el pivoteo.

    Returns:
    Ab: Matriz aumentada después del pivoteo parcial.
    """

    mayor = abs(Ab[k, k])  # Valor absoluto del elemento de pivote actual.
    maxrow = k  # Índice de la fila con el mayor valor absoluto en la columna k.

    # Busca la fila con el mayor valor absoluto en la columna k.
    for s in range(k + 1, n):
        if abs(Ab[s, k]) > mayor:
            mayor = abs(Ab[s, k])
            maxrow = s

    # Verifica si el mayor valor encontrado es cero, lo que indicaría un problema en la solución.
    if mayor == 0:
        print('El sistema no tiene solución única')
    # Si se encontró una fila con un valor más alto, intercambia las filas.
    elif maxrow != k:
        Ab[[k, maxrow]] = Ab[[maxrow, k]]

    return Ab
