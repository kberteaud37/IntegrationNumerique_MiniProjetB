def f(list_coef,x):
    y = 0
    exposant = 0
    for i in list_coef:
        y += i*x**exposant
        exposant += 1
    return y
p1 = 3
p2 = 2
p3 = 4
borne_inf = -25
borne_sup = 25



def python_trapeze (list_coef,borne_inf,borne_sup,n):
    pas = (borne_sup-borne_inf)/n
    surface = 0
    for i in range(borne_inf,borne_sup+1,n):
        T = ((i+pas)-i)*(f(list_coef,i)+f(list_coef,i+pas))
        surface += T
    print(surface)
    return surface






python_trapeze([1,2,3,4],-10,10,20)

