def pozKlucz(*args, **kwargs):
    for index, argument in enumerate(args):
        print("{index} -> {argument}".format(index=index+1, argument=argument))
    print("\n")
    for key, value in kwargs.items():
        print("{key} -> {value}".format(key=key, value=value))

        
lista = [1,2,3,4,5]
slownik = {"smietana": 4, "banany": 3, "mleko": 2, "ser": 4}

pozKlucz(*lista, **slownik)

