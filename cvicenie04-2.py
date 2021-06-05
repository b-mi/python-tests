# Úloha 2
# opäť budeme pracovať so simulátorom kocky, ale v tomto prípade použijeme
# grafickú plochu na vykreslenie výsledku.

import tkinter
import random

canvas_width = 640
canvas_height = 480
canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

number = random.randint(1,6)

print("Na kocke padlo číslo {}".format(number))
print("Vykreslujem kocku...")

# skús iné veľkosti kocky, všetky ostatné výpočty sa prispôsobia
size = 400

# center of dice
x, y = canvas_width / 2, canvas_height / 2
unit = size / 5
radius = size*0.03

# Použi polygon ako obrys kocky. "radius" použijeme na vypočítanie zoseknutia
#
#    p2___p3
# p1/       \p4
#   |       |
#   |       |
# p8\_______/p5
#   p7    p6
#
 
p1 = x - size / 2,  y-size / 2 + radius
p2 = x - size / 2 + radius, y - size / 2
p3 = x + size / 2 - radius, y - size / 2
p4 = x + size / 2,  y-size / 2 + radius
p5 = x + size / 2,  y+size / 2 - radius
p6 = x + size / 2 - radius, y + size / 2
p7 = x - size / 2 + radius, y + size / 2
p8 = x - size / 2,  y+size / 2 - radius

canvas.create_polygon(p1, p2, p3, p4, p5, p6, p7, p8,
                      outline="black", fill="gray", width=3)

# Tu si vypočítame všetky súradnice bodiek dopredu.
# Skús prečítať tento kód a pochopiť ako funguje. Do svojho riešenia skús
# v skratke opísať akým spôsobom sa počítajú všetky body.
# 
# nápoveda:
#
#        a a a
#        1 2 3
#      +-------+
#   b1 | 1   2 |
#   b2 | 3 4 5 |
#   b3 | 6   7 |
#      +-------+
#

r = unit / 2
a1 = x - 1.5*unit - r
a2 = x - r
a3 = x + 1.5*unit - r

b1 = y - 1.5*unit - r
b2 = y - r
b3 = y + 1.5*unit - r


x1, y1 = a1, b1
x2, y2 = a3, b1
x3, y3 = a1, b2
x4, y4 = a2, b2
x5, y5 = a3, b2
x6, y6 = a1, b3
x7, y7 = a3, b3

####### tvoj opis #######
#
# Sem zadaj opis riešenia ako sa
# počítajú jednotlivé bodky na kocke
# 'unit' tam je na rozdelenie plochy pre bodky na patiny
# Nasledne sa suradnice bodiek odvodzuju od stredu kocky x, y s posunom o podiel unit do 4 stran (o 1.5 unitu),
# stredna je priamo v strede na x suradnci.
# Potom sa vytvaraju jednotlive dvojice suradnic (x1, y1), (x2, y2) pre kazdu bodku, pocnuc prvou vlavo hore,
# po riadkoch, zlava do prava. Cize vsetko je pripravene len to naladovat do kocky
# Len som to tam musel posunut o radius, aby som to mal jednoduchsie, to si ale nikto nevsimne.
# Funguje to pekne aj po zmene vekosti kocky
########## end ##########

# Kreslenie bodiek!
# tu začína úloha na logické podmienky. Cieľom je aby si použil(a) na
# vykreslenie každej bodky na kocke len jedno volanie "canvas.create_oval(...)"
# To znamená, že spolu tu bude iba 7 volaní "create_oval"
# Trik spočíva v tom, že musíš sledovať pri ktorých číslach sa vykreslí ktorá
# bodka. Napríklad stredná bodka sa vykresluje len keď padne 1, 3 alebo 5.
# Nevieš súradnice bodky? Použi (x1, y1) ako stred kružnice a "unit" ako
# PRIEMER kružnice ( priemer = 2*polomer ). Takýmto spôsobom sme vykreslovali
# kružnice v lekcí s grafikou.
#
# Nápoveda: riešenie spolu obsahuje 4 volania "if ..." a 7 volaní "create_oval"
# To je 11 riadkov kódu...

######## riešenie zapíš sem ########
#if number > 2: # malovanie 1 bodky
if number > 2:
    canvas.create_oval(x1, y1, x1 + unit, y1 + unit, fill="lightyellow")    # bodka 1
    canvas.create_oval(x7, y7, x7 + unit, y7 + unit, fill="lightyellow")    # bodka 7
if number > 3:
    canvas.create_oval(x2, y2, x2 + unit, y2 + unit, fill="lightyellow")    # bodka 2
    canvas.create_oval(x6, y6, x6 + unit, y6 + unit, fill="lightyellow")    # bodka 6
if number == 2 or number == 6:
    canvas.create_oval(x3, y3, x3 + unit, y3 + unit, fill="lightyellow")    # bodka 3
    canvas.create_oval(x5, y5, x5 + unit, y5 + unit, fill="lightyellow")    # bodka 5
if number % 2 == 1:
    canvas.create_oval(x4, y4, x4 + unit, y4 + unit, fill="lightyellow")    # bodka 4 (stredova)

############### end ################

canvas.mainloop()

