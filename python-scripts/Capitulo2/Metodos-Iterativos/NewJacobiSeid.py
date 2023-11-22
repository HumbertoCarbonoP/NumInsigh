def NewJacobiSeid(x0, A, b, met):
    """
    Calcula la siguiente aproximación a la solución del sistema Ax = b usando el método de Jacobi o Gauss-Seidel.

    Args:
    x0: Vector inicial de aproximación.
    A: Matriz de coeficientes del sistema.
    b: Vector de términos constantes.
    met: Método a utilizar (0 para Jacobi, 1 para Gauss-Seidel).

    Returns:
    x1: Siguiente aproximación a la solución del sistema.
    """

    n = len(A)  # Número de ecuaciones (y dimensiones de la matriz A).
    x1 = x0.copy()  # Copia del vector inicial para evitar la modificación en lugar.

    for i in range(n):  # Itera sobre cada ecuación.
        suma = 0  # Suma inicial para calcular la nueva aproximación de la i-ésima variable.
        
        for j in range(n):  # Itera sobre cada término de la ecuación.
            if j != i:
                if met == 0:  # Método de Jacobi: utiliza el valor anterior de x0.
                    suma += A[i, j] * x0[j]
                elif met == 1:  # Método de Gauss-Seidel: utiliza el nuevo valor de x1 si está disponible.
                    suma += A[i, j] * x1[j]

        # Actualiza la aproximación para la i-ésima variable.
        x1[i] = (b[i] - suma) / A[i, i]

    return x1
