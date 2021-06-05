import random

print("""

 ______                             ______  _           _ 
|  ___ \            _              |  ___ \(_)         | |
| | _ | | ____  ___| |_  ____  ____| | _ | |_ ____   _ | |
| || || |/ _  |/___)  _)/ _  )/ ___) || || | |  _ \ / || |
| || || ( ( | |___ | |_( (/ /| |   | || || | | | | ( (_| |
|_||_||_|\_||_(___/ \___)____)_|   |_||_||_|_|_| |_|\____|
                                                          

""")

meno = input("Zadaj meno hráča: ")
if not meno:
    meno = 'Hráč'

print(f"""

Vitaj {meno.capitalize()}.
Pravidlá sú nasledovné. Ja si myslím číslo od 1 do 10 a ty budeš hádať.
Ak chceš ukončiť hru, napíš 'Koniec'.
Na konci hry uvidíš svoje skóre.

""")

game_over = False
ok_tips = bad_tips = 0
while not game_over:
    print("Myslím si číslo...")
    random_number = random.randint(1, 10)
    player_tip = -1
    while random_number != player_tip:
        player_input = input("Tvoj tip?: ").strip()
        if not player_input:  # nezadana hodnota, znova poziadat o vstup
            print("Neplatná hodnota, zadaj čísla od 1 do 10, alebo 'koniec'")
            continue

        # test ukoncenia proglramu
        if player_input.lower() == 'koniec':
            game_over = True;
            break;

        # kontrola validity vstupu
        if player_input not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
            print("Neplatná hodnota, zadaj čísla od 1 do 10, alebo 'koniec'")
            continue;

        player_tip = int(player_input)
        if random_number == player_tip:
            print("SPRAVNE!\n")
            ok_tips += 1
        else:
            print("NESPRAVNE!")
            bad_tips += 1

print(f"""
+----tvoje skóre-----+
| správne   |  {ok_tips:>4}  |   
| nesprávne |  {bad_tips:>4}  |
| celkom    |  {ok_tips+bad_tips:>4}  |
+--------------------+
""")