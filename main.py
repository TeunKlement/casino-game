from games.roulette import play_roulette
from games.fruitmachine import fruitmachine_spelen
from games.blackjack import play_blackjack
from profiles import (create_account,
                      initialize_player,
                      show_account,
                      show_all_players,
                      switch_account,
                      get_current_balance,
                      update_current_balance,
                      register_played_game,
                      remove_account
                      )

ENTREE_FEE = 10
FREE_MANDATORY_DRINK = 3.50
GAMBLE_TAX = 2
TOTAL_MANDATORY_COST = ENTREE_FEE + FREE_MANDATORY_DRINK + GAMBLE_TAX

def show_main_menu():
    print(f"Casino de Gouden Driehoek - hoofdmenu\n{"-"* 41}\n1. Spellen\n2. Saldo\n3. Account\n0. Stop\n")

def show_account_menu():
    print(f"Casino de Gouden Driehoek - accounts\n{"-"* 41}\n1. Toon alle accounts\n2. Nieuw account\n3. Wissel account\n4. Verwijder account\n0. Stop\n")

def show_games_menu():
    print(f"Casino de Gouden Driehoek - spellen\n{"-" * 41}\n1. Fruitmachine\n2. Roulette\n3. Blackjack\n0. Terug\n")

def show_balance(balance):
    print(f"{"-" * 41}\nHuidig saldo: € {balance:.2f}\n{"-" * 41}")

def main():
    initialize_player(TOTAL_MANDATORY_COST)

    while True:
        show_main_menu()
        choice = int(input("Maak een keuze tussen de 0 en de 3: "))
        match choice:
            case 0:
                print(f"Eindsaldo: {get_current_balance():.2f}")
                break
            case 1:
                show_games_menu()
                game_choice = int(input("kies een waarde tussen 0 en 3: "))
                match game_choice:
                    case 0:
                        continue
                    case 1:
                        balance = fruitmachine_spelen(get_current_balance())
                        update_current_balance(balance)
                        register_played_game('fruitmachine')
                    case 2:
                        balance = play_roulette(get_current_balance())
                        update_current_balance(balance)
                        register_played_game('roulette')
                    case 3:
                        balance = play_blackjack(get_current_balance())
                        update_current_balance(balance)
                        register_played_game('blackjack')
                    case _:
                        print("ongeldige invoer, probeer opnieuw")
            case 2:
                show_balance(get_current_balance())
            case 3:
                show_account()
                show_account_menu()
                account_choice = int(input("Kies een waarde tussen 0 en 4: "))
                match account_choice:
                    case 0:
                        continue
                    case 1:
                        show_all_players()
                    case 2:
                        create_account(TOTAL_MANDATORY_COST)
                    case 3:
                        switch_account()
                    case 4:
                        remove_account()
                    case _:
                        print("ongeldige invoer, probeer opnieuw")
            case _:
                print("ongeldige invoer, probeer opniew")

        if get_current_balance() == 0:
            print("Je hebt geen saldo meer, het spel wordt afgebroken")
            break


main()