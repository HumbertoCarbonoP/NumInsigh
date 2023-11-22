import numpy as np
import NewJacobiSeid

def Iterativos(x0, A, b, Tol, niter, met):
    """
    Calcula la solución del sistema Ax = b usando métodos iterativos.

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
    """

    c = 0  # Contador de iteraciones.
    error = Tol + 1  # Inicializa el error mayor que la tolerancia.
    E = []  # Lista para almacenar el error en cada iteración.

    while error > Tol and c < niter:
        x1 = NewJacobiSeid(x0, A, b, met)  # Función de iteración (no implementada aquí).
        E.append(np.linalg.norm(x1 - x0, np.inf))  # Calcula el error con la norma infinita.
        error = E[-1]  # Actualiza el error.
        x0 = x1  # Actualiza el vector de aproximación.
        c += 1  # Incrementa el contador de iteraciones.

    if error < Tol:
        s = x0  # Solución aproximada.
        n = c  # Número de iteraciones realizadas.
        print(f'La aproximación de la solución del sistema con una tolerancia de {Tol} es: {s}')
        print('            n                Error')
        for i in range(n):
            print(f'{i + 1}                {E[i]}')
    else:
        s = x0
        n = c
        print(f'Fracasó en {niter} iteraciones')

    return E, s
