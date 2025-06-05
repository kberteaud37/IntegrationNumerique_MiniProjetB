import matplotlib.pyplot as plt
import numpy as np

def integration_rectangle(list_coef,borne_inf,borne_sup):

    air = 0
    n = 100  # nombre de rectangles

    largeur = (borne_sup - borne_inf) / n  # largeur de chaque rectangle

    x_vals = []
    y_vals = []
    
    for i in range(n+1):
        x = borne_inf + i * largeur
        y = list_coef[0] + list_coef[1] * x + list_coef[2] * x**2 + list_coef[3] * x**3

        # Tracer le rectangle
        # plt.plot([x - (largeur/2), x + (largeur/2)], [y, y], color='red')
        # plt.plot([x - (largeur/2) , x - (largeur/2)], [0, y], color='red')
        # plt.plot([x + (largeur/2), x + (largeur/2)], [0, y], color='red')

        air += largeur * y

        x_vals.append(x)
        y_vals.append(y)

    print(f"Aire approximée sous la courbe  : {air}")



    # Tracé de la courbe aussi si tu veux
    # plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue', label='Courbe')
    # plt.title("Tracé de l'équation polynomiale avec intégration par rectangles")
    # plt.xlabel("x")
    # plt.ylabel("f(x)")
    # plt.grid(True)
    # plt.legend()
    # plt.show()

    return air


def f(list_coef,x):
    y = 0
    exposant = 0
    for i in list_coef:
        y += i*x**exposant
        exposant += 1
    return y


   
def primitive(list_coef,borne_inf,borne_sup):
    F_a = 0
    F_b = 0
    exposant = 1
    for i in list_coef:
        F_a += i*(borne_inf**exposant/exposant)
        F_b += i*(borne_sup**exposant/exposant)
        exposant += 1
    return F_b-F_a

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

    return A_trapeze
  
def simpson(list_coef,borne_inf,borne_sup,n):
    intervalle = (borne_sup-borne_inf)/n
    a = borne_inf
    A_simpson = 0
    for i in range(n):
        b = a+intervalle
        A_simpson += ((b-a)/6)*(f(list_coef,a)+4*f(list_coef,(a+b)/2)+f(list_coef,b))
        a = b
    return A_simpson

def erreur(list_coef,borne_inf,borne_sup,n,fonction):
    return abs(fonction(list_coef,borne_inf,borne_sup,n)-primitive(list_coef,borne_inf,borne_sup))
  
""" # Calculs
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
plt.show()"""

