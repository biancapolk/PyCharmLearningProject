# WAR.PY
# CARD
# SUIT, RANK, VALUE
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = {'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
playing = True

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        # All 52 card objects
        self.deck = []
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

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

# CONSIDER TABLE CLASS VS PLAYER CLASS
# GAME SETUP

if __name__ == "__main__":

    # Creating a new instance of the Deck class
    new_deck = Deck()

    player_one = Player("One")
    player_two = Player("One")

    player_one.add_cards(new_deck.deal())
    player_two.add_cards(new_deck.deal())

    game_on = True

    round_num = 0

    while game_on:
        round_num += 1
        print(f"Round {round_num}")
        if len(player_one.all_cards) == 0:
            print('Player One, out of cards! Player Two Wins!')
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            print('Player One, out of cards! Player Two Wins!')
            game_on = False
            break
        # START A NEW ROUND
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())

        player_two_cards = []
        player_two_cards.append(player_two.remove_one())

        at_war = True
        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one_cards.add_cards(player_one_cards)
                player_one_cards.add_cards(player_two_cards)
                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_one_cards.add_cards(player_one_cards)
                player_one_cards.add_cards(player_two_cards)
                at_war = False
            else:
                print('WAR!!!')

                if len(player_one.all_cards) < 3:
                    print('Player One unable to declare war')
                    print('PLAYER TWO WINS')
                    game_on = False
                    break

                elif len(player_two.all_cards) < 3:
                    print('Player Two unable to declare war')
                    print('PLAYER ONE WINS')
                    game_on = False
                    break
                else:
                    for num in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())








    # first_card = new_deck.all_cards[-1]
    # print(first_card)


    # try:
    #
    #     five_of_hearts = Card("Hearts", 'Five')
    # except:
    #     print("Sorry, something went wrong. Check that the title of the suit and rank are capitalized")
    # else:
    #     print(five_of_hearts.value)



    # Loop through all of the cards in and new deck and print each card object
    # for card_object in new_deck.all_cards:
    #   print(card_object)


    new_deck.shuffle()
    mycard = new_deck.deal()
    print(mycard)
    print(new_deck.all_cards[0])
    new_player = Player("Jose")
    print(new_player)
    new_player.add_cards()
    new_player()