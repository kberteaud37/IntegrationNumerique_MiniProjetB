import matplotlib.pyplot as plt

def integration_rectangle () :
    p1 = float(input('veuillez entrer la constante p1 : '))
    p2 = float(input('veuillez entrer la constante p2 : '))
    p3 = float(input('veuillez entrer la constante p3 : '))
    p4 = float(input('veuillez entrer la constante p4 : '))

    # borne_inferieur = input('veuillez entrer la borne inferieur : ')
    # borne_superieur = input('veuillez entrer la borne superieur : ')

    x_vals = [-100000]
    y_vals = [100000]

    n = 10
    for i in range (-25,25,n):
        equation = ((p1) +
                    (p2) *(i) +
                    (p3) * (i)**2 +
                    (p4)  *(i)**3)

    plt.plot(x_vals, y_vals, marker='o', linestyle='-')
    plt.title("Tracé de l'équation polynomiale")
    plt.xlabel("i")
    plt.ylabel("Valeur de l'équation")
    plt.grid(True)
    plt.show()


integration_rectangle()


print