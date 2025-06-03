def f(list_coef,x):
    y = 0
    exposant = 0
    for i in list_coef:
        y += i*x**exposant
        exposant += 1
    return y

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





