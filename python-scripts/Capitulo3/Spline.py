import numpy as np

def Spline(x, y, d):
    n = len(x)
    A = np.zeros(((d + 1) * (n - 1), (d + 1) * (n - 1)))
    b = np.zeros((d + 1) * (n - 1))

    if d == 1:
        # Interpolación spline lineal.
        for i in range(n - 1):
            A[i * 2][i * 2] = x[i]
            A[i * 2][i * 2 + 1] = 1
            b[i * 2] = y[i]
            
            A[i * 2 + 1][i * 2] = x[i + 1]
            A[i * 2 + 1][i * 2 + 1] = 1
            b[i * 2 + 1] = y[i + 1]

    elif d == 2:
        # Interpolación spline cuadrática.
        c = 0
        h = 1
        for i in range(n - 1):
            A[i, c] = x[i]**2
            A[i, c + 1] = x[i]
            A[i, c + 2] = 1
            b[i] = y[i]
            c += 3
            h += 1

        c = 0
        for i in range(1, n):
            A[h, c] = x[i]**2
            A[h, c + 1] = x[i]
            A[h, c + 2] = 1
            b[h] = y[i]
            c += 3
            h += 1

        c = 0
        for i in range(1, n - 1):
            A[h, c] = 2 * x[i]
            A[h, c + 1] = 1
            A[h, c + 3] = -2 * x[i]
            A[h, c + 4] = -1
            b[h] = 0
            c += 3
            h += 1

        A[h, 0] = 2
        b[h] = 0

    elif d == 3:
        # Interpolación spline cúbica.
        c = 0
        h = 1
        for i in range(n - 1):
            A[i, c] = x[i]**3
            A[i, c + 1] = x[i]**2
            A[i, c + 2] = x[i]
            A[i, c + 3] = 1
            b[i] = y[i]
            c += 4
            h += 1

        c = 0
        for i in range(1, n):
            A[h, c] = x[i]**3
            A[h, c + 1] = x[i]**2
            A[h, c + 2] = x[i]
            A[h, c + 3] = 1
            b[h] = y[i]
            c += 4
            h += 1

        c = 0
        for i in range(1, n - 1):
            A[h, c] = 3 * x[i]**2
            A[h, c + 1] = 2 * x[i]
            A[h, c + 2] = 1
            A[h, c + 4] = -3 * x[i]**2
            A[h, c + 5] = -2 * x[i]
            A[h, c + 6] = -1
            b[h] = 0
            c += 4
            h += 1

        c = 0
        for i in range(1, n - 1):
            A[h, c] = 6 * x[i]
            A[h, c + 1] = 2
            A[h, c + 4] = -6 * x[i]
            A[h, c + 5] = -2
            b[h] = 0
            c += 4
            h += 1

        A[h, 0] = 6 * x[0]
        A[h, 1] = 2
        b[h] = 0
        h += 1
        A[h, -4] = 6 * x[-1]
        A[h, -3] = 2
        b[h] = 0

    val = np.linalg.solve(A, b)
    Tabla = val.reshape(n - 1, d + 1)

    return Tabla