import random
SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
hand_dealer = []
hand_player = []
hide_card = False

def create_deck():
    deck = [f"{suit}{rank}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def draw_card(deck):
    card = deck.pop()
    return card

def show_hand_dealer(hiden_card):
    if not hiden_card:
        print(f"Dealer hand: {hand_dealer[0]} | {"??"}")
    else:
        print(f"Dealer hand: {" | ".join(hand_dealer)}")

def show_hand_player():
    print(f"Jouw hand: {" | ".join(hand_player)}")

def calculate_hand_value(hand):
    total = sum(calculate_card_value(card) for card in hand)
    number_of_aces = sum(1 for card in hand if card[1] == "A")
    while total > 21 and number_of_aces > 0:
        total -= 10
        number_of_aces -= 1
    return total

def calculate_card_value(card):
    rank = card[1:]
    if rank in ["J", "Q", "K"]:
        return 10
    if rank == "A":
        return 11
    return int(rank)

def play_blackjack(balance):
    print(f"{"-" * 41}\nCasino de Gouden Driehoek - blackjack\n{"-" * 41}\nJe staat op het punt om blackjack te spelen\n\nHet spel werkt als volgt:\nZet een bedrag in\n- Dealer bust is 2 keer je inzet terug\n- Hogere hand dan dealer is 1.5 keer je inzet\n- Gelijke hand is inzet weer terug\n- Bust je zelf dan verlies je je inzet\n{"-" * 41}")
    stake = float(input("Hoeveel geld wil je deze ronde inzetten?: "))
    while stake > balance:
        print(f"{"-" * 41}\nJe hebt momenteel € {balance:.2f} in je wallet, dit is minder dan je wilt inzetten. Dit mag niet, maak opnieuw een spelkeuze.\n{"-" * 41}")
        stake = float(input("Hoeveel geld wil je deze ronde inzetten?: "))
    balance -= stake

    deck = create_deck()

    hand_dealer.append(draw_card(deck))
    hand_dealer.append(draw_card(deck))
    hand_player.append(draw_card(deck))
    hand_player.append(draw_card(deck))

    print(f"Huidige saldo: € {balance:.2f}\nJe inzet: € {stake:.2f}\n")
    global hide_card
    show_hand_dealer(hide_card)
    show_hand_player()
    print(f"Jouw totaal: {calculate_hand_value(hand_player)}")

    while calculate_hand_value(hand_player) < 21:
        choice = input(f"\nKies hit of stand:")
        if choice == "stand":
            break
        elif choice == "hit":
            card = draw_card(deck)
            hand_player.append(card)
            print(f"Je trekt: {card}")
            show_hand_player()
            print(f"Jouw totaal: {calculate_hand_value(hand_player)}")
        else :
            print("verkeerde invoer, probeer opniew")
            continue

    if calculate_hand_value(hand_player) > 21:
        print(f"Je bent \"bust\" en hebt je inzet verloren.\nNieuw saldo: € {balance:.2f}")
        return balance

    hide_card = True
    show_hand_dealer(hide_card)
    while calculate_hand_value(hand_dealer) < 17:
        card = draw_card(deck)
        hand_dealer.append(card)
        print(f"Dealer trekt: {card}")
        show_hand_dealer(hide_card)
        print(f"Dealer totaal: {calculate_hand_value(hand_dealer)}\n")

    if calculate_hand_value(hand_dealer) > 21:
        print(f"De dealer is \"bust\" 2 maal je € {stake:.2f} is toegevoegd aan je balans.")
        balance += stake * 2
    elif calculate_hand_value(hand_player) > calculate_hand_value(hand_dealer):
        print(f"Je hebt een hogere hand dan de dealer. 1.5 maal je inzet, € {stake:.2f}, is toegevoegd aan je balans")
        balance += stake * 1.5
    elif calculate_hand_value(hand_player) == calculate_hand_value(hand_dealer):
        print(f"Je hebt dezelfde hand als de dealer. Je inzet, € {stake:.2f}, is weer toegevoegd aan je balans")
        balance += stake * 1
    else :
        print(f"Je hebt een lagere hand dan de dealer. Je hebt je inleg verloren")

    print(f"{"-" * 41}\nNieuw saldo: € {balance:.2f}\n{"-" * 41}")
    return balance