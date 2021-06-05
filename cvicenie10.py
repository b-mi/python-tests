import tkinter as tk
import random

width, height = 800, 600
sq_8_size = 50
canvas = tk.Canvas(width=width, height=height)
canvas.pack()


def mouse_click(event):
    global sq_1_red_id, sq_1_red_dragged, sq_1_red_pos_diff
    x, y = event.x, event.y
    sq_8_clicked = False

    # zistenie, ci sa nekliklo na red stvorec
    x1, y1, x2, y2 = canvas.coords(sq_1_red_id)
    if x1 <= x < x2 and y1 <= y < y2:
        sq_1_red_dragged = True
        sq_1_red_pos_diff = (x - x1, y - y1)

    if sq_1_red_dragged:
        return

    # zistenie, ci sa nekliklo na jeden z 8 stvorcov
    for rid in sq_8_ids:
        x1, y1, x2, y2 = canvas.coords(rid)
        if x1 <= x < x2 and y1 <= y < y2:
            sq_8_clicked = True
            color = f"#{random.randint(0, 256 ** 3):06X}"
            canvas.itemconfig(rid, fill=color)

    # ak nebol kliknuty stvorec
    if not sq_8_clicked:
        canvas.create_text(event.x, event.y, text=f"({event.x}, {event.y})", font="arial 6")


def create_8_squares():
    sq_8_x = width // 2 - 4 * sq_8_size
    sq_8_y = height // 2.0 - sq_8_size // 2
    y2 = sq_8_y + sq_8_size
    for x in range(sq_8_x, sq_8_x + 8 * sq_8_size, sq_8_size):
        sq_8_ids.append(canvas.create_rectangle(x, sq_8_y, x + sq_8_size, y2))


def create_1_red_square():
    global sq_1_red_id
    x, y = random.randint(0, width - sq_8_size), random.randint(0, height - sq_8_size)
    sq_1_red_id = canvas.create_rectangle(x, y, x + sq_8_size, y + sq_8_size, fill="red")
    pass


def drag_red_square(event):
    global sq_1_red_dragged, sq_1_red_pos_diff, sq_1_red_id
    if sq_1_red_dragged:
        diffx, diffy = sq_1_red_pos_diff  # ponechanie kurzora mysi v tahanom stvorci na relativne rovnakej pozicii
        canvas.moveto(sq_1_red_id, event.x - diffx, event.y - diffy)


def release_red_square(event):
    # ak sa tahal cerveny stvorec, prave sa jeho tahanie skoncilo
    global sq_1_red_dragged
    sq_1_red_dragged = False


def key_press(event):
    x, y = random.randint(0, width - sq_8_size), random.randint(0, height - sq_8_size)
    fsize = random.randint(8, 30)
    canvas.create_text(x, y, text=event.char, font=f"arial {fsize}")


sq_8_ids = []
sq_1_red_id = 0
sq_1_red_dragged = False
sq_1_red_pos_diff = []

canvas.bind("<ButtonPress-1>", mouse_click)
canvas.bind("<B1-Motion>", drag_red_square)
canvas.bind("<ButtonRelease-1>", release_red_square)
canvas.bind_all("<Key>", key_press)
create_8_squares()
create_1_red_square()

canvas.focus_force()
canvas.mainloop()
