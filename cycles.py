import tkinter
import random

canvas = tkinter.Canvas(width=540, height=480)
canvas.pack()
for i in range(10000):
    x = random.randrange(640)
    y = random.randrange(480)
    if y > x:
        farba = "red"
    else:
        farba = "blue"
    canvas.create_oval(x, y, x + 10, y + 10, outline=farba)
canvas.mainloop()