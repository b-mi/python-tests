"""
Dokumentacny string
"""
a, b, c, d = "ahoj"
print(a)
print(b)
print(c)
print(d)

meno = input("Zadaj meno: ")
pocet_znakov = len(meno)
print("Ahoj " + meno + "! Tvoje meno ma " + str(pocet_znakov) + " znakov")
print("Ahoj {}! Tvoje meno ma {} znakov".format(meno, pocet_znakov))
print("Ahoj {meno}! Tvoje meno ma {pocet} znakov".format(meno=meno, pocet=pocet_znakov))
print("'{:<30}'".format('abc'))
print("'{:>30}'".format('abc'))
print("'{:-^30}'".format(' abc '))
print("{:,}".format(12253635))

print(f"{meno}")
