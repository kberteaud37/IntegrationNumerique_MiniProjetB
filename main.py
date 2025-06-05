"""---------------Mini-Projet B - Intégration Numérique----------------------

    - Kilian Berteaud
    - Enzo Villamandos
    - Lucas Bonneaud

Cours MGA802, Session Été 2025
"""

#PROGRAMME PRINCIPAL

from fonctions import *
from fonctions_numpy import *
import matplotlib.pyplot as plt

print("Entrez les coefficients de la fonction f(x)")
liste_coef = []
for i in ["p1","p2","p3","p4"]:
    liste_coef.append(int(input(f"{i} = ")))

print("Entrez l'intervalle de calcul")
borne_inf = 0
borne_sup = 0
while borne_inf>=borne_sup:
    borne_inf = int(input("Entrez la borne inférieure : "))
    borne_sup = int(input("Entrez la borne supérieure : "))

erreur_rectangle = []
erreur_trapeze = []
erreur_simpson = []
nb_segment = []
for i in range(1,20):
    erreur_simpson.append(erreur(liste_coef,borne_inf,borne_sup,i,simpson(liste_coef,borne_inf,borne_sup,i)))
    erreur_trapeze.append(erreur(liste_coef,borne_inf,borne_sup,i,trapeze(liste_coef,borne_inf,borne_sup,i)))
    nb_segment.append(i)


plt.figure(1)
"""plt.plot(nb_segment,erreur_rectangle,'r')"""
plt.plot(nb_segment,erreur_trapeze,'b')
plt.plot(nb_segment,erreur_simpson,'g')
plt.show()