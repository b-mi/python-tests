import tkinter
import os
canvas = tkinter.Canvas(width=1920/2, height=1080/2)
canvas.pack()
canvas.create_line(10, 20, 30, 40)
canvas.create_line(50, 80, 300, 10, 10, 20, 30, 40, fill="red", width=3)

canvas.create_rectangle(30, 30, 400, 400, fill="dodgerblue", width=7, outline="gold")

canvas.create_oval(0, 0, 50, 50, fill="gray", width=2, outline="magenta")

a = (10, 10)
b = (300, 300)
c = (300, 10)
canvas.create_polygon(a, b, c, a, fill="cyan")

canvas.create_text(340, 444, text = "Pytón", font="Monaco 30", fill="green")


cwd = os.getcwd()
print(cwd)

obrazok = tkinter.PhotoImage(file='python_logo.png')
canvas.create_image(150, 150, image=obrazok)
canvas.config(bg="white")

canvas.itemconfig(2, fill="yellow")
canvas.move(2, -5, 3)
canvas.delete(3)

canvas.mainloop()