# WAR.PY
# CARD
# SUIT, RANK, VALUE
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        # All 52 card objects
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)


if __name__ == "__main__":
    try:

        five_of_hearts = Card("Hearts", 'Five')
    except:
        print("Sorry, something went wrong. Check that the title of the suit and rank are capitalized")
    else:
        print(five_of_hearts.value)

new_deck = Deck()
first_card = new_deck.all_cards[-1]
print(first_card)

for card_object in new_deck.all_cards:
    print(card_object)