"""---------------Mini-Projet B - Intégration Numérique----------------------

    - Kilian Berteaud
    - Enzo Villamandos
    - Lucas Bonneaud

Cours MGA802, Session Été 2025
"""

#PROGRAMME PRINCIPAL

from fonctions import *
import fonctions_numpy
import matplotlib.pyplot as plt

from fonctions_numpy import integration_rectangle_numpy

print("Entrez les coefficients de la fonction f(x)")
liste = []
for i in ["p1","p2","p3","p4"]:
    liste.append(int(input(f"{i} = ")))

print("Entrez l'intervalle de calcul")
borne_inf = 0
borne_sup = 0
while borne_inf>=borne_sup:
    borne_inf = int(input("Entrez la borne inférieure : "))
    borne_sup = int(input("Entrez la borne supérieure : "))


print(integration_rectangle_numpy(liste,borne_inf,borne_sup,100))
