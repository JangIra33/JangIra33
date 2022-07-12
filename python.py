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