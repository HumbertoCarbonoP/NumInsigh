import numpy as np
import math

def biseccion(func_str, xi, xs, tol, niter):
    exec(f'def f(x): return {func_str}', globals())

    fi = f(xi)
    fs = f(xs)

    if fi == 0:
        return f'{xi} es raíz de f(x), encontrado en 0 iteraciones'
    elif fs == 0:
        return f'{xs} es raíz de f(x), encontrado en 0 iteraciones'
    elif fs * fi < 0:
        xm = (xi + xs) / 2
        fm = [f(xm)]
        xm_out = [xm]
        error = tol + 1
        error_out = [error]
        xi_out = [xi]
        xs_out = [xs]
        c = 0
        c_out = []

        while error > tol and fm[-1] != 0 and c < niter:
            if fi * fm[-1] < 0:
                xs = xm
                fs = f(xs)
            else:
                xi = xm
                fi = f(xi)
            xa = xm
            xm = (xi + xs) / 2
            error = abs(xm - xa)
            fm.append(f(xm))
            xm_out.append(xm)
            error_out.append(error)
            xi_out.append(xi)
            xs_out.append(xs)
            c_out.append(c+1)
            c += 1
        c_out.append(c+1)

        if fm[-1] == 0:
            print(f'{xm} es raíz de f(x)')
        elif error < tol:
            xm = f'{xm} es una aproximación a una raíz de f(x) con una tolerancia = {tol}'
        else:
            xm= f'Fracasó en {niter} iteraciones'
        
        return xm, c_out, xi_out, xm_out, xs_out, fm, error_out
    else:
        return 'El intervalo es inadecuado'


# Ejemplo de uso:
# s, E, fm = biseccion(0, 2, 0.5e-5, 100)
# print('Resultado:', s, E, fm)
# s, E, fm = biseccion(0, 2, 1e-5, 100)
