import tkinter

width, height = 640, 480


def title(msg):
    print()
    print(chr(31) * 30)
    print(f"{msg:^30}")
    print(chr(30) * 30)


# --------------------------

title("Uloha 1 - delitele")


def list_all_divisors(number):
    # optimalizacia - len do polovice, nad polovicu to nema zmysel zistovat
    pole = [x for x in range(2, number // 2 + 1) if number % x == 0]
    pole.insert(0, 1)  # 1 je vzdy
    pole.append(number)  # cislo same je vzdy
    return pole


for num in 6, 24, 23, 22, 21, 28, 3000, 30001, 496:
    print(f"Delitele {num}: {list_all_divisors(num)}")


# --------------------------
def is_perfect(number):
    if number == 1:
        return False;
    divs = list_all_divisors(number)
    sum: int = 0
    for i in divs:
        sum += i
    sum -= number;
    return sum == number


title("Uloha 2 - perfect nums")
print("Najdenie perfect numbers v rozsahu 1-500")
for num in range(1, 500):
    perf = is_perfect(num)
    if perf:
        print(f"{num} is perfect")

# --------------------------
title("Uloha 4 - transform")


def transform(dct):
    return list(dct.items())


A = {1: "one", 2: "two"}
print(f"{A}: {transform(A)}")

# --------------------------
title("Uloha 5 - merge")


def merge(a, b):
    res = a.copy()
    for bk, bv in b.items():
        if res.__contains__(bk):
            res[bk] = list((res[bk], bv))  # estli tam bol predtym list, asi to bude list listov
        else:
            res[bk] = bv
    return res


A = {1: "one", 2: "two"}
B = {2: "dva", 3: "three", 4: "four"}

print(f"A: {A}")
print(f"B: {B}")
print(f"merge: {merge(A, B)}")

# --------------------------

title("Uloha 3 - snowman")
canvas = tkinter.Canvas(width=width, height=height, bg="lightblue")
canvas.pack()


def ball(x, y, r):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill='white', outline="white")


def snowman(x, y, r):
    ball(x, y, r)

    # druha gula
    new_r = r * 2 / 3
    y -= r + new_r
    ball(x, y, new_r)

    # tretia gula
    r = new_r
    new_r = r * 1 / 2
    y -= r + new_r
    ball(x, y, new_r)


snowman(200, 400, 90)
snowman(400, 300, 45)
snowman(100, 200, 30)

canvas.mainloop()
