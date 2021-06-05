import tkinter
import random

canvas = tkinter.Canvas(width=640, height=480, bg="gray")
canvas.pack()

def kresli_stvorec(x, y, velkost, farba):
    half = velkost / 2
    surad = x - half, y - half, x + half, y + half
    canvas.create_rectangle(surad, fill=farba)

def vzdialenost(x, y):
    return ((x-320)**2 + (y - 240)**2)**.5


def farba(vzd):
    x = 255 - int((vzd / 400) * 255)
    return f"#{x:02x}{x:02x}{x:02x}"

for x in range(1000):
    x = random.randrange(640)
    y = random.randrange(480)
    vzd = vzdialenost(x, y)
    far = farba(vzd)
    kresli_stvorec(x, y, vzd / 6, far)

canvas.mainloop()
