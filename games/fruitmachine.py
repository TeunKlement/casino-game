import random

def fruitmachine_spelen(balance):
        while True:
            print(f"{"-" * 41}\nCasino de Gouden Driehoek - fruitmachine\n{"-" * 41}\nJe staat op het punt op de fruitmachine te spelen en hebt meerdere opties:\n\n0. Stop\n1. Huidige saldo\n2. Spelen\n")
            choice = int(input("Maak een keuze tussen de 0 en de 2: "))
            match choice:
                case 0:
                    break
                case 1:
                    print(f"\n{"-" * 41}\nHuidige saldo: €{balance:.2f}")
                    continue
                case 2:
                    pass
                case _:
                    print("ongeldige invoer, probeer opnieuw")
            print(f"{"-" * 41}\nDe fruitmachine:\n\nHet spel werkt als volgt:\nZet een bedrag in\nBij 2 dezelfde waarden 1.5 keer je inzet.\nBij 3 dezelfde waarden 3.5 keer je inzet.\n{"-" * 41}")
            choice = input("Wil je spelen?[Y/N] ")
            if choice == "Y" or choice == "y":
                pass
            else :
                print(f"{"-" * 41}\nOngeldige invoer\n{"-" * 41}")
                break
            stake = float(input("Hoeveel geld wil je deze ronde inzetten?: "))
            if stake <= 0:
                print("Je moet meer inzetten dan €0, probeer opnieuw.")
                continue
            elif stake > balance:
                print(f"{"-" * 41}\nJe hebt momenteel €{balance:.2f} in je wallet, dit is minder dan je wilt inzetten. Dit mag niet, maak opnieuw een spelkeuze.")
                continue

            balance -= stake

            symbolen = "🍒", "🍋", "⭐"

            random_number_slot1 = random.choice(symbolen)
            random_number_slot2 = random.choice(symbolen)
            random_number_slot3 = random.choice(symbolen)
            print(f"\n     {random_number_slot1}          {random_number_slot2}          {random_number_slot3}\n")

            gerold = [random_number_slot1, random_number_slot2, random_number_slot3]

            if len(set(gerold)) == 1:
                print("DING DING DING, 3 dezelfde\n\nJe krijgt 3.5 keer je inzet.")
                balance += stake * 3.5
            elif len(set(gerold)) == 2:
                print("DING DING, 2 dezelfde\n\nJe krijgt 1.5 keer je inzet.")
                balance += stake * 1.5
            else :
                print("Helaas, bananenkaas.\nJe hebt niks gewonnen...")
        return balance