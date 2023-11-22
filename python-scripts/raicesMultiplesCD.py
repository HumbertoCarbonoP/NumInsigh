import math

def RaicesMultiplesDecimalesCorrectos(m, func_str, func_deriv_str, x_inicial, tolerancia, max_iter):
    # Define la función y su derivada usando exec()
    exec(f"def funcion(x): return {func_str}", globals())
    exec(f"def funcionDerivada(x): return {func_deriv_str}", globals())

    c = 0
    fx = funcion(x_inicial)
    fxPrima = funcionDerivada(x_inicial)
    error = tolerancia + 1
    xn = [x_inicial]
    valores_f = [fx]
    errores = [error]
    iteraciones = []

    while error > tolerancia and abs(fx) > tolerancia and abs(fxPrima) > tolerancia and c < max_iter:
        xn.append(x_inicial - m * (fx / fxPrima))
        fx = funcion(xn[-1])
        fxPrima = funcionDerivada(xn[-1])
        errores.append(abs(xn[-1] - xn[-2]))
        valores_f.append(fx)
        error = errores[-1]
        x_inicial = xn[-1]
        c += 1
        iteraciones.append(c)
    iteraciones.append(c)
    raiz = xn[-1]

    return raiz, iteraciones, valores_f, errores

# Ejemplo de uso:
# raiz, iteraciones, valores_f, errores = RaicesMultiplesDecimalesCorrectos(
#     "math.log(x+100)*((x**2)+((3*6*x)/2)+(9*36)/16)", 
#     "1/(x+100) + 2*x + 9/2", 
#     0, 0.5e-5, 100, 1)
# print('Resultado:', raiz, iteraciones, valores_f, errores)
