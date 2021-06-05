print("-" * 20)
print("Uloha 1")
print("-" * 20)

dice = """+-------+
| {}   {} |
| {} {} {} |
| {}   {} |
+-------+"""

print(dice.format(' ', ' ', ' ', 'o', ' ', ' ', ' '))  # 1
print(dice.format(' ', ' ', 'o', ' ', 'o', ' ', ' '))  # 2
print(dice.format('o', ' ', ' ', 'o', ' ', ' ', 'o'))  # 3
print(dice.format('o', 'o', ' ', ' ', ' ', 'o', 'o'))  # 4
print(dice.format('o', 'o', ' ', 'o', ' ', 'o', 'o'))  # 5
print(dice.format('o', 'o', 'o', ' ', 'o', 'o', 'o'))  # 6

print("-" * 20)
print("Uloha 2")
print("-" * 20)
cislo = int(input("Zadaj cislo: "))
print(f"{cislo:0>32b}") # dost humus

print("-" * 20)
print("Uloha 3")
print("-" * 20)
sirka_stlpca = int(input("Zarovnaj tabulku na sirku stlpca: "))
print(f"+{'tabuľka číselných sústav':-^{(sirka_stlpca + 3)*4 - 1}}+")
print(f"| {'dec':^{sirka_stlpca}} | {'bin':^{sirka_stlpca}} | {'oct':^{sirka_stlpca}} | {'hex':^{sirka_stlpca}} |") # dost jako humus, ale da sa
print(f"+{'':-^{(sirka_stlpca + 3)*4 - 1}}+")
for i in range(0, 15):
    print(f"| {i:>{sirka_stlpca}d} | {i:>{sirka_stlpca}b} | {i:>{sirka_stlpca}o} | {i:>{sirka_stlpca}X} |")
print(f"+{'':-^{(sirka_stlpca + 3)*4 - 1}}+")
