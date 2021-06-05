# uloha 1
cisla = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nove_cisla = [x for x in cisla if x % 2 == 0]
print(nove_cisla)

# uloha 2
cisla = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [round(q) for q in cisla if q > 0]
print(newlist)

# uloha 3
veta = "the quick brown fox jumps over the lazy dog"
slova_dlzka = [len(w) for w in veta.split() if w != 'the']
print(slova_dlzka)