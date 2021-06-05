## Úloha 1
#
# Nakresli 9 pretínajúcich sa kruhov tak ako je to na obrázku spýtaj sa
# používateľa na veľkosť kruhu.  Definuj si najprv súradnice stredného kruhu
# a ostatné odvoď od týchto súradníc
#
# použi nasledujúcu konštrukciu
import tkinter

canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadaj polomer kruznice v nejakom rozumnom rozsahu: "))
w, h = 640, 480
d = r + r
cx, cy = w / 2 - d, h / 2 - d
for row in range(0, 3):
    y = cy + row * r
    for col in range(0, 3):
        x = cx + col * r
        canvas.create_oval(x, y, x + d, y + d, width=2)

canvas.mainloop()


## Úloha 2
#
# Nakresli olympíjske kruhy. Opýtaj sa používateľa na polomer kruhov a na
# súradnice prvého kruhu. pomocou výpočtov potom zisti súradnice všetkých
# ostatných kruhov. Všimni si, že kruhy sa na X-ovej osi nedotýkajú. Je tam
# istý offset. Offset nastav ako 2% z veľkosti polomeru.

import tkinter
canvas = tkinter.Canvas(width=640, height=480)
canvas.pack()

r = int(input("Zadaj polomer olympijského kruhu v nejakom rozumnom rozsahu: "))
d = r + r
x = int(input("Zadaj x súradnicu prvého kruhu v nejakom rozumnom rozsahu: "))
y = int(input("Zadaj y súradnicu prvého kruhu v nejakom rozumnom rozsahu: "))
dx = r * 6 * 0.02 # distancia 2%
colors = ['dodgerblue', 'goldenrod', 'black', 'green', 'red']
sign = 1

for i in range(5):
    canvas.create_oval(x, y, x + d, y + d, width=6, outline=colors[i] )
    x += r + dx / 2
    y += r * sign
    sign = -sign

canvas.mainloop()

