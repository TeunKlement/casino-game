from rich.console import Console
from rich.table import Table
from rich.panel import Panel
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
console = Console()

def show_main_menu():
    table = Table(expand=True)
    table.add_column('Optie')
    table.add_column('Actie')
    table.add_row('1.', 'Spellen')
    table.add_row('2.', 'Saldo')
    table.add_row('3.', 'Account')
    table.add_row('0.', 'Stop')
    console.print(Panel.fit(table, title='De gouden driehoek - hoofdmenu'))

def show_account_menu():
    table = Table(expand=True)
    table.add_column('Optie')
    table.add_column('Actie')
    table.add_row('1.', 'Toon alle accounts')
    table.add_row('2.', 'Nieuw account')
    table.add_row('3.', 'Wissel account')
    table.add_row('4.', 'Verwijder account')
    table.add_row('0.', 'Stop')
    console.print(Panel.fit((table), title='De gouden driehoek - account'))

def show_games_menu():
    table = Table(expand=True)
    table.add_column('Optie')
    table.add_column('Spel')
    table.add_row('1.', 'Fruitmachine')
    table.add_row('2.', 'Roulette')
    table.add_row('3.', 'Blackjack')
    table.add_row('0.', 'Terug')
    console.print(Panel.fit(table, title='De gouden driehoek - spellen'))

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