import tkinter as tk
import random
from datetime import datetime

width, height = 800, 600
ca = tk.Canvas(width=width, height=height)
ca.pack()


def dig_watch():
    global dw_id
    now = datetime.now().time()
    s_time = f"{now.hour:02}:{now.minute:02}:{now.second:02}.{now.microsecond // 100000}"
    ca.itemconfig(dw_id, text=s_time)
    ca.after(100, dig_watch)


def square_task_2():
    global sqt2_id


def sqt2_start_move():
    global sqt2_id, sqt2_dir, sqt2_run, sqt2_size
    if not sqt2_run:
        return
    x, y, _, _ = ca.coords(sqt2_id)
    new_y = y + 5 * sqt2_dir
    if new_y < 0 or new_y >= height - sqt2_size:
        sqt2_dir = -sqt2_dir
    ca.move(sqt2_id, 0, 5 * sqt2_dir)
    if sqt2_run:
        ca.after(20, sqt2_start_move)


def mouse_press(event):
    global sqt2_id, sqt2_run
    sqt2_run = not sqt2_run
    if sqt2_run:
        sqt2_start_move()


# dig hodinky uloha 1
dw_id = ca.create_text(10, 20, anchor=tk.W)
dig_watch()

# stvorcek uloha 2
sqt2_size = 50
sqt2_id = ca.create_rectangle(width // 2, height // 2, width // 2 + sqt2_size, height // 2 + sqt2_size, fill='red')
sqt2_dir = -1  # smer stvorceka
sqt2_run = False  # ci stvorcek chodi
ca.bind("<1>", mouse_press)
square_task_2()

# postreh uloha 3


ca.mainloop()
