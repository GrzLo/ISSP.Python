from math import sqrt as sqrt

def pobierz():
    a = int(input("Podaj współczynnik a: "))
    b = int(input("Podaj współczynnik b: "))
    c = int(input("Podaj współczynnik c: "))
    return a,b,c

def drukuj(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print("Trójmian kwadratowy {a}x^2 + {b}x +{c}:\n Delta = {delta}\n x1 = {x1}\n x2 = {x2}".format(a=a, b=b, c=c, delta=delta, x1=x1, x2=x2))
    elif delta == 0:
        x = (-b + sqrt(delta))/(2*a)
        print("Trójmian kwadratowy {a}x^2 + {b}x +{c}:\n Delta = {delta}\n x = {x}".format(a=a, b=b, c=c, delta=delta, x=x))
    else:
        print("Delta jest mniejsza od 0, brak rozwiązań")

a,b,c = pobierz()
drukuj(a,b,c)
