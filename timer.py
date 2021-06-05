import tkinter as tk

canvas = tk.Canvas(width=800, height=600)
canvas.pack()


def tik():
    print('tik')
    canvas.after(500, tik)


tik()

canvas.mainloop()
