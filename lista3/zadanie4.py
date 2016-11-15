#!/usr/bin/env python

# lista zakupów
grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
# ilość sztuk
n_items = []
# zakazane produkty
prohibited = ['wódka', 'piwo', 'wino']

# w pętli pytamy użytkownika, ile sztuk danego produktu chce kupić
for product in grocery:
    if product in prohibited:
        item = 0
    else:
        item = input("Produkt {productName}: sztuk = ".format(productName=product))
    n_items.append(item)

    # wydrukuj na ekranie komunikat: "Produkt [nazwa produktu]: sztuk = "
    # pobierz liczbę od użytkownika i zapisz w n_items
    # pomiń produkty zakazane (i automatycznie przyjmij ilość = 0)

# drukujemy listę zakupów

print("{:-^50}".format("Lista zakupów"), end="\n\n")
for index, (product, item) in enumerate(zip(grocery, n_items)):
    print("{lp}. {productName:>5} {amount}".format(lp=index+1, productName=product, amount=item))

# w pętli wydrukuj: [lp]. [nazwa produktu]: [ilość]
# czyli np.: 1. jajka: 5 itd.
