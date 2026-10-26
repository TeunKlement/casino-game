MIN_AGE = 18
players = {'Teun': {'naam': 'Teun', "geboortedatum": '20-1-1998', 'gender': 'M', 'saldo': 30, 'gespeelde_spellen': {},},
           'John': {'naam': 'John', 'geboortedatum': '4-4-1997', 'gender': 'M', 'saldo': 20, 'gespeelde_spellen': {},},
           'Annely': {'naam': 'Annely', 'geboortedatum': '9-10-1998', 'gender': 'V', 'saldo': 35, 'gespeelde_spellen': {},}}
current_player = ""

def get_current_balance():
    return players[current_player]['saldo']

def update_current_balance(balance):
    players[current_player]['saldo'] = balance

def register_played_game(game_name):
    played_games = players[current_player]['gespeelde_spellen']
    if game_name in played_games:
        played_games[game_name] += 1
    else :
        played_games[game_name] = 1

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

def create_account(total_mandatory_cost, name=None):
    global current_player
    if name is None:
        name = input("Naam voor het nieuwe account: ").capitalize()
        if name in players:
            print("Dit account bestaat al. Gebruik wissel account om het te openen.")
            return

    gender = input("Wat is je gender?(M/V): ")
    while gender not in ("M", "V"):
        print("Je hebt een verkeerde waarde ingevuld. Vul M of V in, het is hoofdletter gevoelig.")
        gender = input("Wat is je gender?(M/V): ")
    birthdate = check_age(input("Wat is je geboortedag?(dd-mm-yyyy): "))

    start_amount = 0
    while start_amount < total_mandatory_cost:
        print("Als je wil spelen moet je meer dan €16.50 opwaarderen.")
        start_amount = float(input("Met hoeveel geld(euro) wil je gaan spelen?: "))

    balance = 0
    balance += start_amount
    balance -= total_mandatory_cost

    players[name] = create_profile(name,birthdate, gender, balance)
    current_player = name
    return

def show_account():
    print(f"Casino de Gouden Driehoek - account\n{"-" * 41}\nNaam: {current_player}\nVerjaardag: {players[current_player]['geboortedatum']}\nAanspreekvorm: {players[current_player]['gender']}\n")
    print(f"Overige speleraccounts: {" | ".join(players)}")

def show_all_players():
    for naam, key in players.items():
        print(f"Speler {naam} | huidige saldo: € {players[naam]['saldo']:.2f}")

def create_profile(name, birthdate, gender, balance):
    return {"naam": name, "geboortedatum": birthdate, "gender": gender, "saldo": balance, "gespeelde_spellen": {},}

def switch_account():
    global current_player
    name = input("Naar welk account wil je switchen? ")
    if name in players:
        current_player = name
    else:
        print("Dit account bestaat niet")
        return

def remove_account():
    global current_player
    name = input("Welk account wil je verwijderen? ")
    if len(players) == 1:
        print("Er is maar 1 account gevonden, deze mag niet verwijderd worden")
        return
    elif name in players:
        del players[name]
        print(f"Overige speleraccounts: {" | ".join(players)}")
        if name == current_player:
            current_player = list(players.keys())[0]
    else:
        print('Naam is niet gevonden, je wordt terug gestuurd naar het menu.')

def initialize_player(total_mandatory_cost):
    global players
    global current_player

    name = input("Wat is je naam? ").capitalize()
    current_player = name

    if name in players:
        profile = players[current_player]
        salutation = determine_salutation(current_player, profile["gender"])
        balance = profile["saldo"]
        print(f"\n{"-" * 41}\nCasino de gouden driehoek\n{"-" * 41}\n{salutation}\n\nWelkom terug!\nJe huidige saldo is: €{balance}")
    else:
        create_account(total_mandatory_cost, name)

        profile = players[current_player]
        balance = profile["saldo"]
        start_amount = balance + total_mandatory_cost
        salutation = determine_salutation(current_player, profile["gender"])
        if start_amount < total_mandatory_cost:
            entree_check = "onvoldoende"
        else:
            entree_check = "voldoende"
        print(f"\n{"-" * 41}\nCasino de gouden driehoek\n{"-" * 41}\n{salutation}\n\nStartbudget: € {start_amount:.2f}\nVaste kosten: €{total_mandatory_cost:.2f}\nSaldo: €{balance:.2f}\n\nJe hebt {entree_check} budget voor toegang tot het casino.")