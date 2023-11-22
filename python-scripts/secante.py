import math

def Secante(func_str, x0, x1, Tol, niter):
    # Define la función f(x) usando exec()
    exec(f"def f(x): return {func_str}", globals())

    f0 = f(x0)
    f1 = f(x1)

    c = 0
    error = Tol + 1
    s = None

    # Crear listas para almacenar los valores en cada iteración
    n_vals = []
    x0_vals = []
    x1_vals = []
    x2_vals = []
    fx2_vals = []
    error_vals = []

    print('     n                 x0                  x1                  x2                 f(x2)               Error')
    print('-----------------------------------------------------------------------------------------------------------------')

    while error > Tol and c < niter:
        x2 = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        f2 = f(x2)

        # Almacenar los valores en las listas
        n_vals.append(c)
        x0_vals.append(x0)
        x1_vals.append(x1)
        x2_vals.append(x2)
        fx2_vals.append(f2)
        error_vals.append(error)

        print(f'{c:5d} {x0:20.10f} {x1:20.10f} {x2:20.10f} {f2:20.10f} {error:20.10f}')

        if abs(f2) < Tol:
            s = x2
            break

        x0 = x1
        x1 = x2
        f0 = f1
        f1 = f2

        error = abs(x1 - x0)
        c += 1

    if s is None:
        s = x2
    E = error

    return n_vals, x0_vals, x1_vals, x2_vals, fx2_vals, error_vals

# Ejemplo de uso:
# s, E, n_vals, x0_vals, x1_vals, x2_vals, fx2_vals, error_vals = Secante("(abs(x))**(x-1) - 2.5*x - 5", -3, -2, 0.5e-5, 100)
# print('Resultado:', s, E)
