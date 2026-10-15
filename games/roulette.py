import random

def play_roulette(balance):
    while True:
        choice = int(input("Welkom bij de roulette tafel. Je hebt 5 keuzes om dit spel te spelen:\n1. Rood\n2. Zwart\n3. Even\n4. Oneven\n5. Een specifiek getal (0 t/m 36)\n0. Stop\n\nMaak een keuze door een nummer te kiezen(0 om te stoppen): "))
        while choice not in (0, 1, 2, 3, 4, 5):
            choice = int(input("Welkom bij de roulette tafel. Je hebt 5 keuzes om dit spel te spelen:\n1. Rood\n2. Zwart\n3. Even\n4. Oneven\n5. Een specifiek getal (0 t/m 36)\n0. Stop\n\nMaak een keuze door een nummer te kiezen tussen de 0 en de 5(0 om te stoppen): "))

        if choice == 0:
            break
        elif choice == 1:
            choice = "Rood"
        elif choice == 2:
            choice = "Zwart"
        elif choice == 3:
            choice = "Even"
        elif choice == 4:
            choice = "Oneven"
        elif choice == 5:
            choice = int(input("Kies een getal tussen de 0 en de 36:"))

        stake = float(input("Hoeveel geld wil je deze ronde inzetten?: "))
        if stake <= 0:
            print("Je moet meer inzetten dan €0, probeer opnieuw.")
            continue
        elif stake > balance:
            print(f"{"-"*41}\nJe hebt momenteel €{balance:.2f} in je wallet, dit is minder dan je wilt inzetten. Dit mag niet, maak opnieuw een spelkeuze.\n{"-" * 41}")
            continue

        balance -= stake

        random_number = random.randint(0, 36)

        if random_number == 0:
            color = "Groen"
            even_odd = "Groen"
        else :
            if random_number <= 18:
                if random_number%2 == 0:
                    color = "Zwart"
                    even_odd = "Even"
                else :
                    color = "Rood"
                    even_odd = "Oneven"
            else :
                if random_number%2 == 0:
                    color = "Rood"
                    even_odd = "Even"
                else :
                    color = "Zwart"
                    even_odd = "Oneven"

        result = False
        if choice in (color, even_odd, random_number):
            result = True
            print("JE HEBT GEWONNEN")
        else :
            print("Je hebt verloren...")

        if result == True:
            balance += stake * 2

        print(f"Je keuze was {choice} en het willekeurige getal was {random_number}, dit is een {color} vak en een {even_odd} getal.\nJe nieuwe saldo is: €{balance:.2f}")
    return balance
