card_deck = input().split()
faro_shuffles = int(input())
shuffle = 0

while True:
    left_deck = []
    right_deck = []
    card_deck_length = len(card_deck) // 2
    shuffled_card_deck = []

    if shuffle == faro_shuffles:
        print(card_deck)
        break

    for card in range(0, card_deck_length):
        left_deck.append(card_deck[card])
    for card in range(card_deck_length, card_deck_length * 2):
        right_deck.append(card_deck[card])

    for left_card in range(0, len(left_deck)):
        shuffled_card_deck.append(left_deck[left_card])
        shuffled_card_deck.append(right_deck[left_card])
    card_deck = shuffled_card_deck
    shuffle += 1
