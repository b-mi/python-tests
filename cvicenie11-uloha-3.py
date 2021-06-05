import math
import tkinter as tk
import random

max_hits = 15 # max. pocet pokusov
width, height = 800, 600


# validovany vstup
def get_number(msg, enter, minv):
    msg2 = f"{msg}, Enter: {enter}, Min: {minv}: "
    while True:
        stri = input(msg2)
        if not stri:
            return enter
        if stri.isnumeric():
            nval = int(stri)
            if nval >= minv:
                return int(stri)


interval = get_number("Zadaj interval v ms", 1000, 100)
r = get_number("Zadaj polomer kruzku v bodoch na obrazovke", 30, 5)
input(f"Hru na postreh zacnes stlacenim klavesy Enter. Mas {max_hits} pokusov.")

ca = tk.Canvas(width=width, height=height)
ca.pack()


def get_new_coords():
    x = random.randint(10, width - 2 * r)
    y = random.randint(10, height - 2 * r)
    return x, y


def update_score():
    global score, score_id, counter
    ca.itemconfig(score_id, text=f"Skore: {score}/{counter}")


def disable_circle():
    global is_circle_disabled, circle_id
    is_circle_disabled = True
    ca.itemconfig(circle_id, fill="gray")


def mouse_click(event):
    global score, circle_id, score_id, counter, is_circle_disabled
    if is_circle_disabled:
        return
    disable_circle()
    x, y, _, _ = ca.coords(circle_id)
    xdiff, ydiff = abs(x + r - event.x), abs(y + r - event.y)
    diff = math.sqrt(xdiff ** 2 + ydiff ** 2)  # pytagoras
    score += 1 if diff <= r else -1
    update_score()


def game_over():
    global score, counter
    disable_circle()
    ca.create_text(width // 2, height // 2, text=f"Tvoje skóre je {score} z {counter}", font="arial 40",
                   anchor=tk.CENTER)
    ca.create_text(width // 2, height // 2 + 60, text="Blahoželáme", font="arial 40", anchor=tk.CENTER)


def run_game():
    global circle_id, counter, is_circle_disabled
    if counter < max_hits:
        x, y = get_new_coords()
        ca.moveto(circle_id, x, y)
        ca.itemconfig(circle_id, fill="red")
        is_circle_disabled = False
        counter += 1
        update_score()
        ca.after(interval, run_game)
    else:
        game_over()


circle_id = ca.create_oval(-100, -100, -100 + 2 * r, -100 + 2 * r, fill="red")
score_id = ca.create_text(width - 80, 2, text="Skóre: 0/0", anchor=tk.NE)
is_circle_disabled = False
counter = 0
score = 0
ca.bind("<1>", mouse_click)

run_game()
ca.focus_force()
ca.mainloop()
