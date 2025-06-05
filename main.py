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
    liste_coef.append(get_float_input(f"{i} = "))

print("Entrez l'intervalle de calcul")
borne_inf = 0
borne_sup = 0
while borne_inf>=borne_sup:
    borne_inf = get_float_input("Entrez la borne inférieure : ")
    borne_sup = get_float_input("Entrez la borne supérieure : ")

erreur_rectangle = []
erreur_trapeze = []
erreur_simpson = []
erreur_simpson_numpy = []
erreur_trapeze_numpy = []
erreur_rectangle_numpy = []
nb_segment = []
for i in range(100,1000):
    erreur_simpson.append(erreur(liste_coef,borne_inf,borne_sup,i,simpson(liste_coef,borne_inf,borne_sup,i)))
    erreur_trapeze.append(erreur(liste_coef,borne_inf,borne_sup,i,trapeze(liste_coef,borne_inf,borne_sup,i)))
    erreur_rectangle.append(erreur(liste_coef,borne_inf,borne_sup,i,rectangle(liste_coef,borne_inf,borne_sup,i)))
    erreur_simpson_numpy.append(erreur(liste_coef, borne_inf, borne_sup, i, simpson_numpy(liste_coef, borne_inf, borne_sup, i)))
    erreur_trapeze_numpy.append(erreur(liste_coef, borne_inf, borne_sup, i, trapeze_numpy(liste_coef, borne_inf, borne_sup, i)))
    erreur_rectangle_numpy.append(erreur(liste_coef, borne_inf, borne_sup, i, rectangle_numpy(liste_coef, borne_inf, borne_sup, i)))
    nb_segment.append(i)


plt.figure(1)
plt.plot(nb_segment,erreur_rectangle,'r', label="Rectangle")
plt.plot(nb_segment,erreur_trapeze,'b',label="Trapeze")
plt.plot(nb_segment,erreur_simpson,'g',label="Simpson")
plt.xlabel("Nombre de segment")
plt.ylabel("Aire sous la courbe")
plt.grid(True)
plt.legend()
plt.title("Convergence l'erreur en fonction du nombre de segment (Python)")
plt.show()

plt.figure(2)
plt.plot(nb_segment,erreur_rectangle_numpy,'r', label="Rectangle")
plt.plot(nb_segment,erreur_trapeze_numpy,'b',label="Trapeze")
plt.plot(nb_segment,erreur_simpson_numpy,'g',label="Simpson")
plt.xlabel("Nombre de segment")
plt.ylabel("Aire sous la courbe")
plt.grid(True)
plt.legend()
plt.title("Convergence l'erreur en fonction du nombre de segment (Numpy)")
plt.show()