import matplotlib.pyplot as plt

def integration_rectangle():
    p1 = float(input('Veuillez entrer la constante p1 : '))
    p2 = float(input('Veuillez entrer la constante p2 : '))
    p3 = float(input('Veuillez entrer la constante p3 : '))
    p4 = float(input('Veuillez entrer la con`stante p4 : '))

    air = 0

    n = 10000  # nombre de rectangles

    borne_sup = float(input('Donnez la borne supérieure : '))
    borne_inf = float(input('Donnez la borne inférieure : '))

    largeur = (borne_sup - borne_inf) / n  # largeur de chaque rectangle

    x_vals = []
    y_vals = []

    for i in range(n+1):
        x = borne_inf + i * largeur
        y = p1 + p2 * x + p3 * x**2 + p4 * x**3

        # Tracer le rectangle
        plt.plot([x - (largeur/2), x + (largeur/2)], [y, y], color='red')
        plt.plot([x - (largeur/2) , x - (largeur/2)], [0, y], color='red')
        plt.plot([x + (largeur/2), x + (largeur/2)], [0, y], color='red')

        air += largeur * y

        x_vals.append(x)
        y_vals.append(y)

    print(f"Aire approximée sous la courbe : {air}")

    # Tracé de la courbe aussi si tu veux
    plt.plot(x_vals, y_vals, marker='o', linestyle='-', color='blue', label='Courbe')
    plt.title("Tracé de l'équation polynomiale avec intégration par rectangles")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

integration_rectangle()