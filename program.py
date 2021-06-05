# uplne lahke neriesim :-)

# max float: 1.7976931348623157e+308

import math
from datetime import date
import random

# pytagoras
print("Pytagoras")
a, b = 10, 14
c = math.sqrt(a ** 2 + b ** 2)
print('prepona by mala byt: {:.2f}'.format(c))
print('-' * 30)

# posledne 3 cifry
print("Posledne 3 cifry")
cislo = input("zadaj dajake velke cislo: ")
print("posledne 3 cifry cisla {} by mohli byt: {}".format(cislo, int(cislo) % 1000))
print('-' * 30)

# simulator kocky
print("na kocke padlo cislo: {}", random.randint(1, 6))
print("na kocke padlo cislo: {}", random.randint(1, 6))
print("na kocke padlo cislo: {}", random.randint(1, 6))
print("na kocke padlo cislo: {}", random.randint(1, 6))
print("na kocke padlo cislo: {}", random.randint(1, 6))
print("na kocke padlo cislo: {}", random.randint(1, 6))
print('-' * 30)

# input os. udajov
meno = input("Zadaj meno: ")
priezvisko = input("Zadaj priezvisko: ")
adresa = input("Zadaj adresu: ")
sdNar = input("Zadaj datum narodenia, format d.m.yyyy: ")

dParts = sdNar.split(sep='.')
dNar = date(int(dParts[2]), int(dParts[1]), int(dParts[0]))
dNow = date.today()

dDiff = dNow - dNar
age = dDiff.days / 365.25
print()
print('-' * 30)
print("Meno: {} {}".format(meno, priezvisko))
print("Vek cca: {:.2f}".format(age))
print("Adresa: {}".format(adresa))
print('-' * 30)