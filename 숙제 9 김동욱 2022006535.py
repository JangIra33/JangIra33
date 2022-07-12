import random 
def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {2,3,4,5,6,7,8,9,10, "J", "Q", "K", "A"}
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((suit,rank))
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

def show_cards(cards, message):
    print(message)
    for card in cards:
        print(' ', card[0], card[1])

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

def count_score(cards):
    score = 0
    number_of_aces = 0
    for card in cards:
        if card[1] == 'A':
            score += 11
        elif card[1] in {'J','Q','K'}:
            score += 10
        else:
            score += card[1]
    while score > 21 and number_of_aces > 0:
        score -= 10
        number_of_aces -= 1
    return score

def blackjack():
    print("Welcome to Softopia Casino")
    deck = fresh_deck()
    chips = 0
    while True:
        print("-----")
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        print("My cards are:")
        print("  **** **")
        print(' ', dealer[1][0], dealer[1][1])
        show_cards(player, "Your cards are:")
        score_dealer = count_score(dealer)
        score_player = count_score(player)
        if score_player == 21:
            print("Blackjack! You won.")
            chips += 2
        else:
            while score_player < 21 and more("Hit? (y/n) "):
                card, deck = hit(deck)
                player.append(card)
                score_player = count_score(player)
                print(" ", card[0], card[1])
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
            else:
                while score_dealer <= 16:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += 1
                elif score_dealer == score_player:
                    print("We draw.")
                elif score_dealer < score_player:
                    print("You won.")
                    chips += 1
                else:
                    print("I won.")
                    chips -= 1
        print("Chips =", chips)
        if not more("Play more? (y/n) "):
            break
    print("-----")
    print("Bye!")

blackjack()