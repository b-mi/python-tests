# Úloha 1
# vezmi riešenie z predchádzajúceho riešenia s formátovaním stringov a
# vykreslovaním kocky. Tentokrát použi modul random na získanie náhodného
# čísla. Vytvor podmienky typu "elif" a vykresli správnu stranu kocky. Na
# vykreslenie použi iba funkciu "format" a "print"
import random

dice = """+-------+
| {}   {} |
| {} {} {} |
| {}   {} |
+-------+"""

cislo = random.randint(1, 6)
print(f"Nahodne cislo: {cislo}")
if cislo == 1:
    print(dice.format(' ', ' ', ' ', 'o', ' ', ' ', ' '))  # 1
elif cislo == 2:
    print(dice.format(' ', ' ', 'o', ' ', 'o', ' ', ' '))  # 2
elif cislo == 3:
    print(dice.format('o', ' ', ' ', 'o', ' ', ' ', 'o'))  # 3
elif cislo == 4:
    print(dice.format('o', 'o', ' ', ' ', ' ', 'o', 'o'))  # 4
elif cislo == 5:
    print(dice.format('o', 'o', ' ', 'o', ' ', 'o', 'o'))  # 5
elif cislo == 6:
    print(dice.format('o', 'o', 'o', ' ', 'o', 'o', 'o'))  # 6
