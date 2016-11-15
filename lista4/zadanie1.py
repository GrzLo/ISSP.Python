products = {"chleb": 3, "masło": 4, "mleko": 2, "makaron": 4, "woda": 1}

for product, price in products.items():
    print(product, price)

print("Średnia cena produktów to:", sum(products.values())/len(products))

products.update(Herbata=4)

print("Średnia cena produktów to:", sum(products.values())/len(products))

del products["masło"]

print("Średnia cena produktów to:", sum(products.values())/len(products))
