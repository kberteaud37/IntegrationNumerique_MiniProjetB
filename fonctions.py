import matplotlib.pyplot as plt
import numpy as np

# Données
coefficients = [1, 2, 3, 4]
borne_inf = -10
borne_sup = 10
n = 100


def f(list_coef, x):
    return sum(coef * x**i for i, coef in enumerate(list_coef))

def trapeze(list_coef, borne_inf, borne_sup, n):
    intervalle = (borne_sup - borne_inf) / n
    a = borne_inf
    A_trapeze = 0
    segments = []

    for _ in range(n):
        b = a + intervalle
        fa = f(list_coef, a)
        fb = f(list_coef, b)
        A_trapeze += (intervalle) * (fa + fb) / 2

        # On stocke les points nécessaires pour tracer les segments
        segments.append((a, fa, b, fb))
        a = b

    return A_trapeze, segments

def primitive(list_coef, borne_inf, borne_sup):
    aire = 0
    for i, coef in enumerate(list_coef):
        expo = i + 1
        aire += coef * (borne_sup**expo - borne_inf**expo) / expo
    return aire



# Calculs
aire_approchee, segments = trapeze(coefficients, borne_inf, borne_sup, n)
aire_exacte = primitive(coefficients, borne_inf, borne_sup)

print(f"Aire approchée (trapèzes, n={n}) : {aire_approchee: }")
print(f"Aire exacte (calculée à la main) : {aire_exacte: }")

# Tracé de la fonction réelle
x_vals = np.linspace(borne_inf, borne_sup, 1000)
y_vals = [f(coefficients, x) for x in x_vals]

plt.plot(x_vals, y_vals, label="f(x)", color="blue")
plt.axhline(0, color='black', linewidth=0.5)

# Affichage des trapèzes
for a, fa, b, fb in segments:
    plt.plot([a, a], [0, fa], color='red')  # côté gauche
    plt.plot([a, b], [fa, fb], color='red')  # sommet
    plt.plot([b, b], [0, fb], color='red')  # côté droit

plt.title("Méthode des trapèzes")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
