import numpy as np

def MatJacobiSeid(x0, A, b, Tol, niter, met):
    """
    Calcula la solución del sistema Ax = b usando una versión matricial de los métodos de Jacobi o Gauss-Seidel.

    Args:
    x0: Vector inicial de aproximación.
    A: Matriz de coeficientes del sistema.
    b: Vector de términos constantes.
    Tol: Tolerancia para el criterio de parada.
    niter: Número máximo de iteraciones.
    met: Método a utilizar (0 para Jacobi, 1 para Gauss-Seidel).

    Returns:
    E: Vector de errores en cada iteración.
    s: Aproximación de la solución al sistema.
    T: Matriz de iteración correspondiente al método seleccionado.
    """

    c = 0  # Contador de iteraciones.
    error = Tol + 1  # Inicializa el error mayor que la tolerancia.
    E = []  # Lista para almacenar el error en cada iteración.

    D = np.diag(np.diag(A))  # Diagonal de A.
    L = -np.tril(A, -1)  # Parte triangular inferior de A (sin diagonal).
    U = -np.triu(A, 1)  # Parte triangular superior de A (sin diagonal).

    while error > Tol and c < niter:
        if met == 0:  # Método de Jacobi.
            T = np.linalg.inv(D) @ (L + U)
            C = np.linalg.inv(D) @ b
        elif met == 1:  # Método de Gauss-Seidel.
            T = np.linalg.inv(D - L) @ U
            C = np.linalg.inv(D - L) @ b

        x1 = T @ x0 + C  # Calcula la nueva aproximación.

        # Calcula el error usando la norma infinita (criterio de parada).
        E.append(np.linalg.norm((x1 - x0) / x1, np.inf))
        error = E[-1]  # Actualiza el error.
        x0 = x1  # Actualiza el vector de aproximación.
        c += 1  # Incrementa el contador de iteraciones.

    if error < Tol:
        s = x0  # Solución aproximada.
        print(f"Numero de iteraciones: {c}")
    else:
        s = x0
        print(f'Fracasó en {niter} iteraciones')

    return E, s, T
