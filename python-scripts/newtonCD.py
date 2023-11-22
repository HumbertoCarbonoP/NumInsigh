import math

def NewtonDecimalesCorrectos(func_str, func_deriv_str, x_inicial, tolerancia, max_iter):
    # Define la función y su derivada usando exec()
    exec(f"def funcion(x): return {func_str}", globals())
    exec(f"def funcionDerivada(x): return {func_deriv_str}", globals())

    c = 0
    valores_f = [funcion(x_inicial)]
    fx = valores_f[c]
    valores_f_primera_derivada = funcionDerivada(x_inicial)
    fxPrima = valores_f_primera_derivada
    errores = [tolerancia + 1]
    error = errores[c]
    xn = [x_inicial]
    n = [c]

    while error > tolerancia and abs(fx) > tolerancia and abs(fxPrima) > tolerancia and c < max_iter:
        xn.append(x_inicial - fx / fxPrima)
        valores_f.append(funcion(xn[-1]))
        fx = valores_f[-1]
        valores_f_primera_derivada = funcionDerivada(xn[-1])
        fxPrima = valores_f_primera_derivada
        errores.append(abs(xn[-1] - xn[-2]))
        error = errores[-1]
        x_inicial = xn[-1]
        n.append(c + 1)
        c += 1

    if abs(fx) <= tolerancia:
        raiz = xn[-1]
        iteraciones = c
        resultado = f'{raiz} es una aproximación de una raíz de f(x) con una tolerancia = {tolerancia}, encontrado en {iteraciones} iteraciones'
    elif fxPrima == 0:
        raiz = xn[-1]
        iteraciones = c
        resultado = f'{raiz} es una posible raíz múltiple de f(x)'
    else:
        raiz = None
        iteraciones = c
        resultado = 'Fracasó en encontrar una raíz con la tolerancia especificada en el número máximo de iteraciones'

    return resultado, n, xn, valores_f, errores

# Ejemplo de uso:
# resultado, n, xn, valores_f, errores = NewtonDecimalesCorrectos(
#     "x**3 - 4*x**2 - 3*x + 18", 
#     "3*x**2 - 8*x - 3", 
#     0, 0.5e-5, 100)
# print('Resultado:', resultado)
