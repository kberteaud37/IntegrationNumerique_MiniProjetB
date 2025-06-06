import numpy as np
from fonctions import f


def trapeze_numpy(list_coef, borne_inf, borne_sup, n):
    #Création du x et du y, en fonction de l'intervalle donnée
    x = np.linspace(borne_inf, borne_sup, n + 1)
    y = f(list_coef, x)

    h = (borne_sup - borne_inf) / n

    aire = h * (y[0] + 2 * np.sum(y[1:-1]) + y[-1]) / 2
    return aire
  
def simpson_numpy(list_coef, borne_inf, borne_sup, n):
    h = (borne_sup - borne_inf) / n

    # Points de départ et fin des sous-intervalles
    a_vals = np.linspace(borne_inf, borne_sup - h, n)
    b_vals = a_vals + h
    m_vals = (a_vals + b_vals) / 2

    # Vectoriser f() pour qu'elle accepte des arrays
    f_vec = np.vectorize(lambda x: f(list_coef, x))

    A_vals = (h / 6) * (
            f_vec(a_vals) + 4 * f_vec(m_vals) + f_vec(b_vals)
    )

    return np.sum(A_vals)


def rectangle_numpy(list_coef, borne_inf, borne_sup, n):
    largeur = (borne_sup - borne_inf) / n  # largeur de chaque rectangle
    #Ajout des valeurs x et y pour chaque segment
    x_milieux = np.linspace(borne_inf + largeur / 2, borne_sup - largeur / 2, n)
    y_milieux = np.polyval(list_coef[::-1], x_milieux)
    #Calcul de l'aire sous la courbe
    aire = np.sum(y_milieux * largeur)

    return aire


