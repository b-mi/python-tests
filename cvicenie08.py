import csv


def title(msg):
    print()
    print(chr(31) * 30)
    print(f"{msg:^30}")
    print(chr(30) * 30)

########################################################
title("Uloha 1")
file_name = input("Meno suboru? ")

print("Teraz zadavaj riadky + Enter, prazdny riadok koniec")
# najskor ho vytvori
with open(file_name, 'w') as fp:
    while True:
        ria = input("")
        if ria:
            fp.write(f"{ria}\n")
        else:
            break

# potom otvori a zisti co treba
with open(file_name, 'r') as fp:
    line = fp.readline()
    print(f"Prve tri znaky 1 riadku: {line[:3]}")

########################################################
title("Uloha 2")
file_name = input("Zadaj meno suboru, alebo enter pre movies.csv ? ")
if not file_name:
    file_name = 'movies.csv'
with open(file_name, 'r') as fp:
    max = 0
    cnt = 0
    line = fp.readline()
    for line in fp:
        lenline = len(line)
        cnt += 1
        if lenline > max:
            max = lenline

    print(f"Pocet riadkov suboru {cnt}")
    print(f"Najdlhsi riadok ma {max - 1} znakov")  # -1 lebo bez /n

########################################################
title("Uloha 3")
movies_year_file = 'movies_year.csv'


def add_year(file_name):
    with open(movies_year_file, 'w') as fpw:
        fpw.write('Rank,Rating,Title,Year, No. of Reviews\n')
        with open(file_name, 'r') as fpr:
            reader = csv.DictReader(fpr)
            for riadok in reader:
                title = riadok["Title"]
                new_title = title[:-7]
                year = title[-5:-1]
                fpw.write(f"{riadok['Rank']},{riadok['Rank']},{new_title},{year},{riadok['No. of Reviews']}\n")


add_year('movies.csv')
print("Vytvoreny file movies_year.csv")

########################################################
title("Uloha 4")

def movies_by_year(year):
    with open(movies_year_file, "r") as fp:
        reader = csv.DictReader(fp);
        for riadok in reader:
            if riadok["Year"] == year:
                print(riadok["Title"])


movies_by_year(input("Zadaj rok, pre ktore chces zoznam filmov? "))
