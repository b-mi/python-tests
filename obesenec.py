import sys
import tkinter
import random

width, height = 640, 480
basex = width // 2
basey = height * 0.7
body_parts = []
used_letters = []
word_letters = []
ok_char_count = 0
word = ''
game_state = 'run'
mistakes_count = 0
canvas = tkinter.Canvas(width=width, height=height)
canvas.pack()


def draw_gibbet():
    canvas.create_rectangle(basex - 150, basey, basex + 150, basey + 20, fill="black")
    canvas.create_line(basex - 100, basey, basex - 100, basey - 300, basex, basey - 300, width=5)
    canvas.create_line(basex, basey - 300, basex, basey - 250, width=1)


def draw_hangman():
    head = canvas.create_oval(basex - 15, basey - 250, basex - 15 + 30, basey - 220, width=2, state=tkinter.HIDDEN)
    body = canvas.create_line(basex, basey - 220, basex, basey - 120, width=6, state=tkinter.HIDDEN)
    larm = canvas.create_line(basex, basey - 200, basex - 30, basey - 150, width=3, state=tkinter.HIDDEN)
    rarm = canvas.create_line(basex, basey - 190, basex + 40, basey - 140, width=3, state=tkinter.HIDDEN)
    lleg = canvas.create_line(basex, basey - 140, basex - 30, basey - 50, width=3, state=tkinter.HIDDEN)
    rleg = canvas.create_line(basex, basey - 130, basex + 40, basey - 40, width=3, state=tkinter.HIDDEN)
    return [head, body, larm, rarm, lleg, rleg]


def init_word(new_word):
    word_width = len(new_word) * 40
    x = (width - word_width) // 2 - 40
    y = height * 0.9
    for c in new_word:
        x += 40
        if c == ' ':
            continue;
        canvas.create_line(x, y, x + 30, y)
        text_id = canvas.create_text(x + 15, y - 20, text=c, font="arial 30", state=tkinter.HIDDEN)
        word_letters.append([c, text_id])


def game_over(msg):
    canvas.create_text(width / 2 + 150, 50, text = msg, font="arial 40", fill='dodgerblue')


def check_input(inp_ch):
    global ok_char_count, mistakes_count, game_state
    lst = [x for x in word_letters if x[0] == inp_ch]
    if len(lst):
        for char_data in lst:
            canvas.itemconfig(char_data[1], state=tkinter.NORMAL)
            ok_char_count += 1
        if ok_char_count == len(word_letters):
            game_state = "win"
            game_over("You win")
    else:
        canvas.itemconfig(body_parts[mistakes_count], state=tkinter.NORMAL)
        mistakes_count += 1
        if mistakes_count == 6:
            game_state = 'loss'
            game_over("You loss")
    # print(f"ok: {ok_char_count}, mist: {mistakes_count}, st: {game_state}")


def set_word():
    global word
    with open('obesenec.txt') as fp:
        lines = fp.read().splitlines()
        word = lines[random.randint(0, len(lines) - 1)]


set_word()
draw_gibbet()
body_parts = draw_hangman()
init_word(word)

while game_state == "run":
    inp = input("Zadaj 1 pismeno a Enter: ");
    if len(inp) != 1:
        continue
    inp = inp.lower()
    if inp in used_letters:
        continue;
    used_letters.append(inp)
    check_input(inp)

canvas.mainloop()