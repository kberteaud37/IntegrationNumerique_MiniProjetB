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
import matplotlib.ticker as ticker
from scipy import integrate

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

valeur_rectangle = []
valeur_trapeze = []
valeur_simpson = []
valeur_primitive = []
valeur_rectangle_numpy = []
valeur_trapeze_numpy = []
valeur_simpson_numpy = []
erreur_rectangle = []
erreur_trapeze = []
erreur_simpson = []
erreur_simpson_numpy = []
erreur_trapeze_numpy = []
erreur_rectangle_numpy = []
valeur_trapz = []
valeur_simps = []
nb_segment = []

for i in range(20,200):
    valeur_rectangle.append(rectangle(liste_coef,borne_inf,borne_sup,i))
    valeur_trapeze.append(trapeze(liste_coef,borne_inf,borne_sup,i))
    valeur_simpson.append(simpson(liste_coef,borne_inf,borne_sup,i))
    valeur_primitive.append(primitive(liste_coef,borne_inf,borne_sup))
    valeur_rectangle_numpy.append(rectangle_numpy(liste_coef,borne_inf,borne_sup,i))
    valeur_trapeze_numpy.append(trapeze_numpy(liste_coef,borne_inf,borne_sup,i))
    valeur_simpson_numpy.append(simpson_numpy(liste_coef,borne_inf,borne_sup,i))
    erreur_simpson.append(erreur(liste_coef,borne_inf,borne_sup,i,simpson(liste_coef,borne_inf,borne_sup,i)))
    erreur_trapeze.append(erreur(liste_coef,borne_inf,borne_sup,i,trapeze(liste_coef,borne_inf,borne_sup,i)))
    erreur_rectangle.append(erreur(liste_coef,borne_inf,borne_sup,i,rectangle(liste_coef,borne_inf,borne_sup,i)))
    erreur_simpson_numpy.append(erreur(liste_coef, borne_inf, borne_sup, i, simpson_numpy(liste_coef, borne_inf, borne_sup, i)))
    erreur_trapeze_numpy.append(erreur(liste_coef, borne_inf, borne_sup, i, trapeze_numpy(liste_coef, borne_inf, borne_sup, i)))
    erreur_rectangle_numpy.append(erreur(liste_coef, borne_inf, borne_sup, i, rectangle_numpy(liste_coef, borne_inf, borne_sup, i)))
    x = np.linspace(borne_inf,borne_sup,i)
    y = f(liste_coef,x)
    valeur_simps.append(float(integrate.simpson(y,x=x)))
    valeur_trapz.append(float(integrate.trapezoid(y,x=x)))
    nb_segment.append(i)

plt.figure(1)
#Enlever la notation scientifique à l'axe y
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
plt.plot(nb_segment,valeur_rectangle,'r', label="Rectangle")
plt.plot(nb_segment,valeur_trapeze,'b',label="Trapeze")
plt.plot(nb_segment,valeur_simpson,'g',label="Simpson")
plt.plot(nb_segment,valeur_primitive,'k',label="Solution exacte")
plt.xlabel("Nombre de segment")
plt.ylabel("Aire sous la courbe")
plt.grid(True)
plt.legend()
plt.title("Convergence de l'aire obtenue en fonction du nombre de segment (Python)")
plt.show()

plt.figure(2)
#Enlever la notation scientifique à l'axe y
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
#Tracer les trois courbes
plt.plot(nb_segment,valeur_rectangle_numpy,'r', label="Rectangle")
plt.plot(nb_segment,valeur_trapeze_numpy,'b',label="Trapeze")
plt.plot(nb_segment,valeur_simpson_numpy,'g',label="Simpson")
plt.plot(nb_segment,valeur_primitive,'k',label="Solution exacte")
#Mettre des légendes
plt.xlabel("Nombre de segment")
plt.ylabel("Aire sous la courbe")
plt.grid(True)
plt.legend()
plt.title("Convergence l'aire obtenue en fonction du nombre de segment (Python)")
plt.show()

plt.figure(3)
#Enlever la notation scientifique à l'axe y
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
plt.plot(nb_segment,erreur_rectangle,'r', label="Rectangle")
plt.plot(nb_segment,erreur_trapeze,'b',label="Trapeze")
plt.plot(nb_segment,erreur_simpson,'g',label="Simpson")
plt.xlabel("Nombre de segment")
plt.ylabel("Erreur entre l'aire obtenue et l'aire exacte")
plt.grid(True)
plt.legend()
plt.title("Convergence de l'erreur en fonction du nombre de segment (Python)")
plt.show()

plt.figure(4)
#Enlever la notation scientifique à l'axe y
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
plt.plot(nb_segment,erreur_rectangle_numpy,'r', label="Rectangle")
plt.plot(nb_segment,erreur_trapeze_numpy,'b',label="Trapeze")
plt.plot(nb_segment,erreur_simpson_numpy,'g',label="Simpson")
plt.xlabel("Nombre de segment")
plt.ylabel("Erreur entre l'aire obtenue et l'aire exacte")
plt.grid(True)
plt.legend()
plt.title("Convergence de l'erreur en fonction du nombre de segment (Numpy)")
plt.show()

plt.figure(5)
#Enlever la notation scientifique à l'axe y
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
plt.plot(nb_segment,valeur_trapz,'r', label="Trapeze (Scipy)")
plt.plot(nb_segment,valeur_trapeze,'b',label="Trapeze")
plt.plot(nb_segment,valeur_trapeze_numpy,'y',label="Trapeze (Numpy)")
plt.xlabel("Nombre de segment")
plt.ylabel("Aire sous la courbe")
plt.grid(True)
plt.legend()
plt.title("Convergence de l'aire obtenue en fonction du nombre de segment")
plt.show()

plt.figure(6)
#Enlever la notation scientifique à l'axe y
ax = plt.gca()
ax.yaxis.set_major_formatter(ticker.ScalarFormatter(useOffset=False))
plt.plot(nb_segment,valeur_simps,'r', label="Simpson (Scipy)")
plt.plot(nb_segment,valeur_simpson,'b',label="Simpson")
plt.plot(nb_segment,valeur_simpson_numpy,'y',label="Simpson (Numpy)")
plt.xlabel("Nombre de segment")
plt.ylabel("Aire sous la courbe")
plt.grid(True)
plt.legend()
plt.title("Convergence de l'aire obtenue en fonction du nombre de segment")
plt.show()