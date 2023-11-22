import math

def reglaFalsa(func_str, xi, xs, Tol, niter):
    # Define la función f(x) usando exec()
    exec(f'def f(x): return {func_str}', globals())

    fi = f(xi)
    fs = f(xs)

    if fi == 0:
        return f'{xi} es raíz de f(x), encontrado en 0 iteraciones', [0], [xi], [fi], [0]
    elif fs == 0:
        return f'{xs} es raíz de f(x), encontrado en 0 iteraciones', [0], [xs], [fs], [0]
    elif fs * fi < 0:
        c = 0
        xm = xs - (fs * (xs - xi)) / (fs - fi)
        fm = [f(xm)]
        E = [abs(xm)]
        xn = [xm]
        N = [c]

        while abs(fm[-1]) > Tol and c < niter:
            if fi * fm[-1] < 0:
                xs = xm
                fs = f(xs)
            else:
                xi = xm
                fi = f(xi)

            xa = xm
            xm = xs - (fs * (xs - xi)) / (fs - fi)
            fm.append(f(xm))
            E.append(abs(xm - xa))
            xn.append(xm)
            N.append(c + 1)
            c += 1

        if abs(fm[-1]) <= Tol:
            return f'{xm} es una aproximación a una raíz de f(x) con una tolerancia = {Tol}, encontrado en {c} iteraciones', N, xn, fm, E
        else:
            return f'Fracasó en {niter} iteraciones', N, xn, fm, E
    else:
        return 'El intervalo es inadecuado', [], [], [], []

# Ejemplo de uso:
# resultado, N, xn, fm, E = ReglaFalsa('math.log(math.sin(x)**2 + 1) - 0.5', 0, 2, 0.5e-5, 100)
# print('Resultado:', resultado)
