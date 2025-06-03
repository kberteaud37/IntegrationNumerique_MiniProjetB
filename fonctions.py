
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

=======
def f(list_coef,x):
    y = 0
    exposant = 0
    for i in list_coef:
        y += i*x**exposant
        exposant += 1
    return y

def primitive(list_coef,borne_inf,borne_sup):
    F_a = 0
    F_b = 0
    exposant = 1
    for i in list_coef:
        F_a += i*(borne_inf**exposant/exposant)
        F_b += i*(borne_sup**exposant/exposant)
        exposant += 1
    return F_b-F_a

def simpson(list_coef,borne_inf,borne_sup,n):
    intervalle = (borne_sup-borne_inf)/n
    a = borne_inf
    A_simpson = 0
    for i in range(n):
        b = a+intervalle
        print(a,b)
        A_simpson += ((b-a)/6)*(f(list_coef,a)+4*f(list_coef,(a+b)/2)+f(list_coef,b))
        a = b
    return A_simpson