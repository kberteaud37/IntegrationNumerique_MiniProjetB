import numpy as np

# Données
coefficients = [1, 2, 3, 4]
borne_inf = -10
borne_sup = 10
n = 100

def primitive(list_coef, borne_inf, borne_sup):
    aire = 0
    for i, coef in enumerate(list_coef):
        expo = i + 1
        aire += coef * (borne_sup**expo - borne_inf**expo) / expo
    return aire


def f(list_coef, x):
    return sum(coef * x**i for i, coef in enumerate(list_coef))

def trapeze_numpy(list_coef, borne_inf, borne_sup, n):
    x = np.linspace(borne_inf, borne_sup, n + 1)
    y = f(list_coef, x)

    h = (borne_sup - borne_inf) / n

    aire = h * (y[0] + 2 * np.sum(y[1:-1]) + y[-1]) / 2
    return aire


# Calculs
aire_numpy = trapeze_numpy(coefficients, borne_inf, borne_sup, n)
aire_exacte = primitive(coefficients, borne_inf, borne_sup)

print(f"Aire approchée (trapèzes, n={n}) : {aire_numpy: }")
print(f"Aire exacte (calculée à la main) : {aire_exacte: }")