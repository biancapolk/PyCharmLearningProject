'''WAR.PY'''
import unittest

'''CARD'''
'''SUIT, RANK, VALUE'''
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
playing = True
'''Card Class'''
class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

'''
Deck Class
'''
class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))  # build Card objects and add them to the list

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


'''
Player Class
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        pass

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List Sof multiple card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

'''
Hand Class
'''
class Hand:

    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
'''
Chips Class
'''
class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

class TestCap(unittest.TestCase):
    def test_deck(self):
        test_deck = Deck()
        print(test_deck)

    def test_player(self):

        test_player = Hand()
        for card in test_player.cards:
            print(card)

    def test_hand(self):
        test_deck = Deck()
        test_deck.shuffle()
        test_player = Hand()
        test_player.add_card(test_deck.deal())
        test_player.add_card(test_deck.deal())
        test_player.value



# GAME SETUP

if __name__ == "__main__":
    test_deck = Deck()
    test_player = Hand()
    test_player.add_card(test_deck.deal())
    test_player.add_card(test_deck.deal())
    test_player.value
    for card in test_player.cards:
        print(card)


    # # Creating a new instance of the Deck class
    # new_deck = Deck()
    #
    # player_one = Player("One")
    # player_two = Player("One")
    #
    # player_one.add_cards(new_deck.deal)
    # player_two.add_cards(new_deck.deal)
    #
    # game_on = True
    #
    # round_num = 0
    #
    # while game_on:
    #     round_num += 1
    #     print(f"Round {round_num}")
    #     if len(player_one.all_cards) == 0:
    #         print('Player One, out of cards! Player Two Wins!')
    #         game_on = False
    #         break
    #     if len(player_two.all_cards) == 0:
    #         print('Player One, out of cards! Player Two Wins!')
    #         game_on = False
    #         break
    #     # START A NEW ROUND
    #     player_one_cards = []
    #     player_one_cards.append(player_one.remove_one())
    #
    #     player_two_cards = []
    #     player_two_cards.append(player_two.remove_one())
    #
    #     at_war = True
    #     while at_war:
    #         if player_one_cards[-1].value > player_two_cards[-1].value:
    #             player_one_cards.add_cards(player_one_cards)
    #             player_one_cards.add_cards(player_two_cards)
    #             at_war = False
    #         elif player_one_cards[-1].value < player_two_cards[-1].value:
    #             player_one_cards.add_cards(player_one_cards)
    #             player_one_cards.add_cards(player_two_cards)
    #             at_war = False
    #         else:
    #             print('WAR!!!')
    #
    #             if len(player_one.all_cards) < 3:
    #                 print('Player One unable to declare war')
    #                 print('PLAYER TWO WINS')
    #                 game_on = False
    #                 break
    #
    #             elif len(player_two.all_cards) < 3:
    #                 print('Player Two unable to declare war')
    #                 print('PLAYER ONE WINS')
    #                 game_on = False
    #                 break
    #             else:
    #                 for num in range(3):
    #                     player_one_cards.append(player_one.remove_one())
    #                     player_two_cards.append(player_two.remove_one())


