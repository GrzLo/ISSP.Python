def mniejsza (a,b):
    if a == b:
        return a
    elif a < b:
        return a
    else:
        return b

def najmniejsza (*args):
    najmniejsza = args[0]
    for liczba in args:
        najmniejsza = mniejsza(najmniejsza, liczba)
    print("Najmniejszą liczbą jest", najmniejsza)

najmniejsza(142,2124,51,425,346,123,112,55,163,24,15,72)
