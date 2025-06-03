def f(list_coef, x):
    return sum(coef * x**i for i, coef in enumerate(list_coef))

def trapeze(list_coef, borne_inf, borne_sup, n):
    """
    Calcule l'intégrale approchée d'un polynôme entre deux bornes
    en utilisant la méthode des trapèzes.
    """
    intervalle = (borne_sup - borne_inf) / n
    a = borne_inf
    A_trapeze = 0
    for _ in range(n):
        b = a + intervalle
        A_trapeze += (intervalle) * (f(list_coef, a) + f(list_coef, b)) / 2
        a = b
    return A_trapeze

def primitive(list_coef, borne_inf, borne_sup):
    """
    Calcule l'intégrale exacte d'un polynôme défini par ses coefficients
    entre deux bornes, sans utiliser de bibliothèque externe.
    """
    aire = 0
    for i, coef in enumerate(list_coef):
        expo = i + 1
        aire += coef * (borne_sup**expo - borne_inf**expo) / expo
    return aire

# Définition du polynôme : f(x) = 1 + 2x + 3x² + 4x³
coefficients = [1, 2, 3, 4]

# Intervalle d'intégration
borne_inf = -10
borne_sup = 10


n = 10

aire_approchee = trapeze(coefficients, borne_inf, borne_sup, n)
aire_exacte = primitive(coefficients, borne_inf, borne_sup)

print(f"Aire approchée (trapèzes, n={n}) : {aire_approchee:.6f}")
print(f"Aire exacte (calculée à la main) : {aire_exacte:.6f}")


