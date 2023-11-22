import numpy as np

def SOR(x0, A, b, Tol, niter, w):
    """
    Calcula la solución del sistema Ax = b usando el método SOR (Gauss-Seidel relajado).

    Args:
    x0: Vector inicial de aproximación.
    A: Matriz de coeficientes del sistema.
    b: Vector de términos constantes.
    Tol: Tolerancia para el criterio de parada.
    niter: Número máximo de iteraciones.
    w: Factor de relajación.

    Returns:
    E: Vector de errores en cada iteración.
    s: Aproximación de la solución al sistema.
    n: Número de iteraciones realizadas.
    T: Matriz de iteración correspondiente al método SOR.
    """

    c = 0  # Contador de iteraciones.
    error = Tol + 1  # Inicializa el error mayor que la tolerancia.
    E = []  # Lista para almacenar el error en cada iteración.

    D = np.diag(np.diag(A))  # Diagonal de A.
    L = -np.tril(A, -1)  # Parte triangular inferior de A (sin diagonal).
    U = -np.triu(A, 1)  # Parte triangular superior de A (sin diagonal).

    while error > Tol and c < niter:
        T = np.linalg.inv(D - w * L) @ ((1 - w) * D + w * U)
        C = w * np.linalg.inv(D - w * L) @ b
        x1 = T @ x0 + C  # Calcula la nueva aproximación.

        # Calcula el error usando la norma infinita (criterio de parada).
        E.append(np.linalg.norm(x1 - x0, np.inf))
        error = E[-1]  # Actualiza el error.
        x0 = x1  # Actualiza el vector de aproximación.
        c += 1  # Incrementa el contador de iteraciones.

    if error < Tol:
        s = x0  # Solución aproximada.
        print(f'Es una aproximación de la solución del sistema con una tolerancia de {Tol}')
    else:
        s = x0
        print(f'Fracasó en {niter} iteraciones')

    return E, s, c, T
