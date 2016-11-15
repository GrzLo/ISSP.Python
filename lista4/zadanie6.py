#nie wiem czy o to chodziło w tym zadaniu
#sama funkcja nie ma na celu robienia czegokolwiek konkretnego
def wymus(a, b, *c, d, e, f):
    suma = 0
    for liczba in c:
        suma+=liczba
    x = (a*b + suma*d) / (e*f)
    print("({a}*{b} + {suma}*{d}) / ({e}*{f})".format(a=a, b=b, suma=suma, d=d, e=e, f=f))
    print(x)

wymus(1,2,3,4,5,6,7,8,9,10, d=11, e=12, f=13)


