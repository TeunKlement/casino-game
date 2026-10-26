from games.roulette import play_roulette
from games.fruitmachine import fruitmachine_spelen
from games.blackjack import play_blackjack

ENTREE_FEE = 10
FREE_MANDATORY_DRINK = 3.50
GAMBLE_TAX = 2
TOTAL_MANDATORY_COST = ENTREE_FEE + FREE_MANDATORY_DRINK + GAMBLE_TAX
MIN_AGE = 18

def show_main_menu():
    print(f"Casino de Gouden Driehoek - hoofdmenu\n{"-"* 41}\n1. Spellen\n2. Saldo\n3. Account\n0. Stop\n")

def show_games_menu():
    print(f"Casino de Gouden Driehoek - spellen\n{"-" * 41}\n1. Fruitmachine\n2. Roulette\n3. Blackjack\n0. Terug\n")

def show_balance(balance):
    print(f"{"-" * 41}\nHuidig saldo: € {balance:.2f}\n{"-" * 41}")

def show_account(name, birthdate, gender):
    print(f"Casino de Gouden Driehoek - account\n{"-" * 41}\nNaam: {name}\nVerjaardag: {birthdate}\nAanspreekvorm: {gender}\n")

def determine_salutation(name, gender):
    if gender == "M":
        return f"Welkom, meneer {name}"
    else :
        return f"Welkom, meneer {name}"

def check_age(birthdate):
    birth_day, birth_month, birth_year = birthdate.split("-")
    age = 2026 - int(birth_year)
    if age < MIN_AGE:
        print("Je bent niet oud genoeg om te gokken. Het programma wordt afgesloten.")
        exit(1)
    else :
        return birthdate

def show_welcome_message(start_amount, balance, entree_check, salutation):
    print(f"\n{"-" * 41}\nCasino de gouden driehoek\n{"-" * 41}\n{salutation}\n\nStartbudget: €{start_amount:.2f}\nVaste kosten: €{TOTAL_MANDATORY_COST:.2f}\nSaldo: €{balance:.2f}\n\nJe hebt {entree_check} budget voor toegang tot het casino.")

def main():
    name = input("Wat is je naam?: ").capitalize()
    gender = input("Wat is je gender?(M/V): ")
    while gender not in ("M", "V"):
        print("Je hebt een verkeerde waarde ingevuld. Vul M of V in, het is hoofdletter gevoelig.")
        gender = input("Wat is je gender?(M/V): ")
    birthdate = check_age(input("Wat is je geboortedag?(dd-mm-yyyy): "))

    salutation = determine_salutation(name, gender)

    start_amount = 0
    while start_amount < TOTAL_MANDATORY_COST:
        print("Als je wil spelen moet je meer dan €16.50 opwaarderen.")
        start_amount = float(input("Met hoeveel geld(euro) wil je gaan spelen?: "))

    balance = 0
    balance += start_amount
    balance -= TOTAL_MANDATORY_COST

    if start_amount < TOTAL_MANDATORY_COST:
        entree_check = "onvoldoende"
    else:
        entree_check = "voldoende"

    show_welcome_message(start_amount, balance, entree_check, salutation)

    while True:
        show_main_menu()
        choice = int(input("Maak een keuze tussen de 0 en de 3: "))
        match choice:
            case 0:
                print(f"Eindsaldo: {balance:.2f}")
                break
            case 1:
                show_games_menu()
                game_choice = int(input("kies een waarde tussen 0 en 3: "))
                match game_choice:
                    case 0:
                        continue
                    case 1:
                        balance = fruitmachine_spelen(balance)
                    case 2:
                        balance = play_roulette(balance)
                    case 3:
                        balance = play_blackjack(balance)
                    case _:
                        print("ongeldige invoer, probeer opnieuw")
            case 2:
                show_balance(balance)
            case 3:
                show_account(name, birthdate, salutation)
            case _:
                print("ongeldige invoer, probeer opniew")

        if balance == 0:
            print("Je hebt geen saldo meer, het spel wordt afgebroken")
            break


main()