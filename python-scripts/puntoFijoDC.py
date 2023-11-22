import math

def PuntoFijoDecimalesCorrectos(x0, Tol, niter):
    # Define f(x) y g(x) usando exec()
    exec("def f(x): return x - 2 * math.sin(math.sqrt(abs(x + 2)))", globals())
    exec("def g(x): return 2 * math.sin(math.sqrt(abs(x + 2)))", globals())

    c = 0
    fm = [f(x0)]
    E = [Tol + 1]
    xn = [x0]
    N = [c]
    error = E[0]

    while error > Tol and abs(fm[-1]) > Tol and c < niter:
        xn.append(g(xn[-1]))
        fm.append(f(xn[-1]))
        E.append(abs(xn[-1] - xn[-2]))
        error = E[-1]
        N.append(c + 1)
        c += 1

    if abs(fm[-1]) <= Tol:
        resultado = f'{xn[-1]} es una aproximación de una raíz de f(x) con una tolerancia = {Tol}, encontrado en {c} iteraciones'
    elif error < Tol:
        resultado = f'{xn[-1]} es una aproximación de una raíz de f(x) con una tolerancia = {Tol}, encontrado en {c} iteraciones'
    else:
        resultado = f'Fracasó en {niter} iteraciones'

    return resultado, N, xn, fm, E

# Ejemplo de uso:
# resultado, N, xn, fm, E = PuntoFijoDecimalesCorrectos(1, 0.5e-5, 100)
# print('Resultado:', resultado)
