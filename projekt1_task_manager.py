# funkce pro přidávání úkolů
def pridat_ukol(ukoly: list) -> None:
    """
    Vyzve uživatele k zadání názvu a popisu úkolu, ošetří vstupy a přidá úkol do seznamu
    """
    print()
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()
        if nazev == "" or popis == "":
            print("Chyba: Musíte vyplnit název i popis!")
        else:
            ukol = {"nazev": nazev, "popis": popis}
            ukoly.append(ukol)
            print("Úkol '" + nazev + "' byl přidán.")
            print()
            return

# funkce pro zobrazení seznamu úkolů
def zobrazit_ukoly(ukoly: list) -> None:
    """
    Vypíše seznam všech vložených úkolů, případně upozorní uživatele na prázdný seznam
    """
    print()
    if not ukoly: #nejdříve kontrola, jeslti seznam není prázdný
        print("V seznamu zatím nejsou žádné úkoly.")
        print()
        return
    print("Seznam úkolů:") #až poté vypsat seznam úkolů
    # enumerate místo ručního čítače
    for cislo, ukol in enumerate(ukoly, start=1):
        print(f"{cislo}. {ukol['nazev']} - {ukol['popis']}")    
    print()

# funkce pro mazání úkolů ze seznamu
def odstranit_ukol(ukoly: list) -> None:
    """
    Vypíše seznam úkolů a umožní uživateli zvolit úkol ke smazání, přitom ošetřuje neexistující indexy a nečíselné vstupy
    """
    zobrazit_ukoly(ukoly)
    if not ukoly:
        return
    cislo_input = input("Zadejte číslo úkolu, který chcete odstranit: ")
    try: #ošetření výjimky - nečíselný vstup
        index = int(cislo_input) - 1
        if 0 <= index < len(ukoly):
            smazany = ukoly.pop(index)
            print("Úkol '" + smazany["nazev"] + "' byl odstraněn.")
        else:
            print("Chyba: Úkol s tímto číslem neexistuje.")
    except ValueError:
         print("Chyba: Zadaný vstup není číslo!")
    print()

# základní funkce - hlavní menu
def hlavni_menu() -> None:
    """
    Spouští smyčku aplikace a zpracovává volby uživatele
    """
    ukoly = []
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat úkol")
        print("2. Zobrazit úkoly")
        print("3. Odstranit úkol")
        print("4. Konec")

        volba = input("Vyberte akci (1-4): ")

        if volba == "1":
            pridat_ukol(ukoly)
        elif volba == "2":
            zobrazit_ukoly(ukoly)
        elif volba == "3":
            odstranit_ukol(ukoly)
        elif volba == "4":
            print("Konec programu")
            break

if __name__ == "__main__":
    hlavni_menu()