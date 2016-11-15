import random

n = random.randint(0, 100)
guess = int(input("Podaj liczbę od 0 do 100\n"))

while guess != n:
    if n - guess > 50:
        guess = int(input("Twoja liczba jest dużo mniejsza\nPodaj nową liczbę\n"))
    elif n - guess > 10:
        guess = int(input("Twoja liczba jest mniejsza\nPodaj nową liczbę\n"))
    elif n - guess > 0 and n - guess <= 10:
        guess = int(input("Twoja liczba jest trochę mniejsza\nPodaj nową liczbę\n"))
    elif n - guess < 0 and n - guess >= -10:
        guess = int(input("Twoja liczba jest trochę większa\nPodaj nową liczbę\n"))
    elif n - guess < -50:
        guess = int(input("Twoja liczba jest dużo większa\nPodaj nową liczbę\n"))
    elif n - guess < -10:
        guess = int(input("Twoja liczba jest większa\nPodaj nową liczbę\n"))

print("Brawo zgadłeś!")
