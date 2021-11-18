import random

def deal_cards(deck, number):
    hand_value = 0 # Initialize an accumulator for the hand value
    hand = {} # Initialize an empty dictionary
    for i in range(number):
        random_card = random.choice(list(deck.keys()))
        print(random_card)
        val = deck[random_card]
        hand_value += val
        deck.pop(random_card)
        hand[random_card] = val # Assign key-value pairs to the handdictionary
    print("Value of this hand: " + str(hand_value))
    return deck, hand

def create_deck():
    deck = {} # Initialize an empty dictionary
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
    for suit in suits:
        for rank in ranks:
            value = 0
            if rank == "Ten" or rank == "Jack" or rank == "Queen" or rank == "King": value = 10
            elif rank == "Ace": value = 11
            elif rank == "Two": value = 2
            elif rank == "Three": value = 3
            elif rank == "Four": value = 4
            elif rank == "Five": value = 5
            elif rank == "Six": value = 6
            elif rank == "Seven": value = 7
            elif rank == "Eight": value = 8
            elif rank == "Nine": value = 9
            deck[rank + " of " + suit] = value # Assign key-value pairs to the deck dictionary
    return deck

def main():
    deck = create_deck() # Creates a deck of cards
    print(len(deck)) # Verifies that 52 cards were created
    deck, hand1 = deal_cards(deck, 2)
    print(len(deck)) # Verifies that 2 cards have been removed
    print(len(hand1)) # Verifies that 2 cards exist
    deck, hand2 = deal_cards(deck, 2)
    print(len(deck)) # Verifies that 2 cards have been removed
    print(len(hand2)) # Verifies that 2 cards exist

main()
