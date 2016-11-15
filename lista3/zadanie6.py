#!/usr/bin/env python

import turtle

#Wlasciwie to mozna trojkat i kwadrat rysowac tez uzywajac kodu z 3 przykladu ale zeby nie bylo to zostawilem wszystko. Mam nadzieje, ze kod jest wystarczajaco czytelny. Domyslnie pierwszy przyklad z trojkatem jest aktywny

length = eval(input("Podaj długość boku: "))
#n_times = eval(input("Podaj ilość wielokątów: ")) #usunac komentarz przy 4 przykladzie

rect_sides = 4 # boki kwadratu
tria_sides = 3 # boki trójkąta
hexa_sides = 6 # boki szesciokatu
#poly_sides = eval(input("Podaj ilość boków wielokątu: ")) #usunac komentarz przy 3 i 4 przykladzie

turtle.speed(20) # ustal prędkość żółwia

#kwadrat
#for i in range(rect_sides):
#    turtle.forward(length)     # narysuj linię o danej długości
#    turtle.right(90)           # obróć się w prawo o dany kąt

#trojkat
for i in range(tria_sides):
    turtle.forward(length)      # narysuj linię o danej długości
    turtle.left(120)            # obróć się w lewo o dany kąt

#szesciokat foremny
#for i in range(hexa_sides):
#    turtle.forward(length)     # narysuj linię o danej długości
#    turtle.right(60)           # obróć się w prawo o dany kąt

#wielokat foremny (usunac komentarz przy poly_sides)
#for i in range(poly_sides):
#    turtle.forward(length)         # narysuj linię o danej długości
#    turtle.right(360/poly_sides)   # obróć się w prawo o dany kąt


#wielokat razy  (usunac komentarz przed poly_sides i n_times)
#for j in range(n_times):
#    turtle.right(360/n_times)          # obróć się w prawo o kąt zależny od ilości wielokątów
#    for i in range(poly_sides):
#        turtle.forward(length)         # narysuj linię o danej długości
#        turtle.right(360/poly_sides)   # obróć się w prawo o dany kąt

turtle.mainloop() # nie zamykaj okna po narysowaniu
