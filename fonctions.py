#Fonction qui retourne la valeur de f(x) pour un x donné
def f(liste_coef, x):
    y = 0
    exposant = 0
    for i in liste_coef:
        y += i * x ** exposant
        exposant += 1
    return y

#Fonction qui calcul simplement la primitive du polynôme
def primitive(liste_coef, borne_inf, borne_sup):
    F_a = 0
    F_b = 0
    exposant = 1
    for i in liste_coef:
        F_a += i * (borne_inf ** exposant / exposant)
        F_b += i * (borne_sup ** exposant / exposant)
        exposant += 1
    return F_b - F_a

def rectangle(liste_coef,borne_inf,borne_sup,n):

    air = 0

    largeur = (borne_sup - borne_inf) / n  # largeur de chaque rectangle

    x_vals = []
    y_vals = []
    
    for i in range(n+1):
        x = borne_inf + i * largeur
        y = liste_coef[0] + liste_coef[1] * x + liste_coef[2] * x**2 + liste_coef[3] * x**3

        air += largeur * y

        x_vals.append(x)
        y_vals.append(y)

    return air

def trapeze(liste_coef, borne_inf, borne_sup, n):
    intervalle = (borne_sup - borne_inf) / n
    a = borne_inf
    A_trapeze = 0
    segments = []

    for _ in range(n):
        b = a + intervalle
        fa = f(liste_coef, a)
        fb = f(liste_coef, b)
        A_trapeze += intervalle * (fa + fb) / 2

        # On stocke les points nécessaires pour tracer les segments
        segments.append((a, fa, b, fb))
        a = b

    return A_trapeze

#Fonction appliquant la méthode Simpson du sujet
def simpson(liste_coef,borne_inf,borne_sup,n):
    #Création de l'intervalle en fonction du nombre de segments donné
    intervalle = (borne_sup-borne_inf)/n
    a = borne_inf
    #Initialisation de l'aire calculée sous la méthode de Simpson
    A_simpson = 0
    for _ in range(n):
        b = a+intervalle
        A_simpson += ((b-a)/6)*(f(liste_coef,a)+4*f(liste_coef,(a+b)/2)+f(liste_coef,b))
        a = b
    return A_simpson

#Fonction qui retourne l'erreur entre la fonction et le calcul de la primitive
def erreur(liste_coef,borne_inf,borne_sup,valeur_fonction):
    return abs(valeur_fonction-primitive(liste_coef,borne_inf,borne_sup))

#Fonction forçant l'utilisateur à entrer une valeur acceptable
def get_float_input(prompt):
    while True:
        # Constantly check if a value was entered followed by Enter
        try:
            # Put the value entered by user in "entrée"
            value = float(input(prompt))
            break
        except ValueError:
            # If input is not a float we get a ValueError
            print("Invalid input, please try again.")
    return value


