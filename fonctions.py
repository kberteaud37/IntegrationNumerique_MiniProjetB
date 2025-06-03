import matplotlib.pyplot as plt

def integration_rectangle () :
    p1 = float(input('veuillez entrer la constante p1 : '))
    p2 = float(input('veuillez entrer la constante p2 : '))
    p3 = float(input('veuillez entrer la constante p3 : '))
    p4 = float(input('veuillez entrer la constante p4 : '))

    air = 0

    n = 1
    for i in range (-10,11,n):
        equation = ((p1) +
                    (p2) *(i) +
                    (p3) * (i)**2 +
                    (p4)  *(i)**3)


        plt.plot([i-(n/2), i+(n/2)], [equation, equation], color='red', linewidth=2, label='Mon segment')
        plt.plot([i-(n/2), i-(n/2)], [equation, 0], color='red', linewidth=2, label='Mon segment')
        plt.plot([i+(n/2), i+(n/2)], [equation, 0], color='red', linewidth=2, label='Mon segment')

        air += (n * (equation))

        plt.plot(i, equation, marker='o', linestyle='-')

    print(air)

    plt.title("Tracé de l'équation polynomiale")
    plt.xlabel("i")
    plt.ylabel("Valeur de l'équation")
    plt.grid(True)
    plt.show()


integration_rectangle()


# Tracer le segment

