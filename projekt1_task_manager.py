ukoly = []

def pridat_ukol():
    print()
    while True:
        nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        if nazev == "" or popis == "":
            print("Chyba: Musíte vyplnit název i popis!")
        else:
            ukol = {"nazev": nazev, "popis": popis}
            ukoly.append(ukol)
            
            print("Úkol '" + nazev + "' byl přidán.")
            print()
            return

def zobrazit_ukoly():
    print()
    print("Seznam úkolů:")
    cislo = 1
    for ukol in ukoly:
        print(str(cislo) + ". " + ukol["nazev"] + " - " + ukol["popis"])
        cislo = cislo + 1
    if not ukoly:
        print("V seznamu zatím nejsou žádné úkoly.")
    print()

def odstranit_ukol():
    zobrazit_ukoly()
    if not ukoly:
        return
    cislo_input = input("Zadejte číslo úkolu, který chcete odstranit: ")
    index = int(cislo_input) - 1
    if 0 <= index < len(ukoly):
        smazany = ukoly.pop(index)
        print("Úkol '" + smazany["nazev"] + "' byl odstraněn.")
    else:
        print("Chyba: Úkol s tímto číslem neexistuje.")
    print()

def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec")

        volba = input("Vyberte akci (1-4): ")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu")
        elif volba == "4":
            print("Konec programu")
            break

hlavni_menu()