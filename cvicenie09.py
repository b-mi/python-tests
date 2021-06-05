import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.pencolor('gray')


def title(msg):
    print()
    print(chr(31) * 30)
    print(f"{msg:^30}")
    print(chr(30) * 30)


def stvorec(size, color):
    t.fillcolor(color)
    t.begin_fill()
    t.setheading(0)  # doprava
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.right(90)
    t.backward(size)


def trojuholnik(size, color):
    t.fillcolor(color)
    t.begin_fill()
    t.seth(60)
    t.forward(size)
    t.right(120)
    t.forward(size)
    t.right(30)
    t.end_fill()
    t.penup()
    t.forward(size)
    t.pendown()


def domcek(size, col_roof, col_wall):
    stvorec(size, col_wall)
    trojuholnik(size, col_roof)


def ulica(sizes):
    for size in sizes:
        domcek(size, 'red', 'blue')
    canvas = s.getcanvas()
    canvas.create_text(-200, -200, text="klik mysou pre ukoncenie")


title("Uloha 1 - domcek")
domcek(100, 'red', 'blue')

# ----------------------------------------------

title("Uloha 2 - ulica")
t.penup()
t.setpos(-200, -100)
t.pendown()
ulica([60, 50, 40, 30, 20, 10])

t.hideturtle()
s.exitonclick()
turtle.TurtleScreen._RUNNING = True  # aby to nehadzalo stale chyby pri opakovanom spusteni

# ----------------------------------------------

title("Uloha 3")

print("Odhadujem ze cca vynasobi parametre - a vyzera ze som trafil, hoci som cakal nejaku kulehu")

# ----------------------------------------------

title("Uloha 4")


def pocet(char, text):
    if not text:
        return 0  # ak je text prazdny s istotou tam nie pozadovane pismeno, ak to teda nie je prazdny znak
    if text[0] == char:
        # ak prvy znak je pozadovany, pripocitame jednotku a pocet tychto znakov zo zbytku textu
        return 1 + pocet(char, text[1:])
    else:
        # ak prvy znak nie je pozadovany, pripocitame nulu a pocet tychto znakov zo zbytku textu
        return 0 + pocet(char, text[1:])


txt = 'mama ma emu a ema ma mamu'
print(txt)
for char in 'm', 'a', ' ', 'x':
    print(f"pocet znaku '{char}': {pocet(char, txt)}")

# ----------------------------------------------

title("Uloha 5")


def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num - 1)


for n in range(10):
    print(f'faktorial cisla {n} by mohol byt {factorial(n)}')
