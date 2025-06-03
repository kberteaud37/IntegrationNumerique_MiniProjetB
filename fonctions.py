def fonction_polynomiale(a,b,c,d,x):
    return a+b*x+c*x**2+d*x**3

def simpson(f_x,borne_inf,borne_sup,n):
    ((borne_sup-borne_inf)/(6))*(f(borne_inf)+4*f((borne_inf+borne_sup)/2)+f(borne_sup))
