"""---------------Mini-Projet B - Intégration Numérique----------------------

    - Kilian Berteaud
    - Enzo Villamandos
    - Lucas Bonneaud

Cours MGA802, Session Été 2025
"""

#PROGRAMME PRINCIPAL

import fonctions
import fonctions_numpy
import matplotlib.pyplot as plt

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

for i in range(100):
