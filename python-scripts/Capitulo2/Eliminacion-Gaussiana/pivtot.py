def pivtot(Ab, mark, n, k):
    """
    Realiza el pivoteo total sobre la matriz aumentada Ab del sistema Ax = b.

    Args:
    Ab: Matriz aumentada del sistema Ax = b.
    mark: Vector que rastrea el orden original de las columnas.
    n: Número total de filas (y columnas) en la matriz Ab.
    k: Índice actual para el pivoteo.

    Returns:
    Ab: Matriz aumentada después del pivoteo total.
    mark: Vector actualizado que rastrea el orden de las columnas.
    """

    mayor = 0  # Valor más alto encontrado para el pivoteo.
    maxrow = maxcol = k  # Índices de la fila y columna con el valor más alto.

    # Busca el mayor valor absoluto en la submatriz que comienza en (k, k).
    for r in range(k, n):
        for s in range(k, n):
            if abs(Ab[r, s]) > mayor:
                mayor = abs(Ab[r, s])
                maxrow, maxcol = r, s

    # Verifica si el mayor valor encontrado es cero, lo que indicaría un problema en la solución.
    if mayor == 0:
        print('El sistema no tiene solución única')
    else:
        # Intercambia filas si es necesario.
        if maxrow != k:
            Ab[[k, maxrow]] = Ab[[maxrow, k]]

        # Intercambia columnas si es necesario y actualiza el vector de marcas.
        if maxcol != k:
            Ab[:, [k, maxcol]] = Ab[:, [maxcol, k]]
            mark[k], mark[maxcol] = mark[maxcol], mark[k]

    return Ab, mark
