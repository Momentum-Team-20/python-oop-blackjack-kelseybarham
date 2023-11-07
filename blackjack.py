import random

# Write your blackjack game here.
# C - card
# R - value, suit, rank, know where it is in deck
# C - Deck
SUITS = ['♥️', '♦️', '♣️', '♠️']
RANKS = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank, value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# C - deck
# R - is shuffled, card dealt from it, holds the cards in an order,
# C - Card


class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                if card.rank == 'A':
                    card.value = (1, 11)
                elif card.rank in range(2, 11):
                    card.value = rank
                else:
                    card.value = 10

                print(card)
                self.cards.append(card)
        print(f'There are {len(self.cards)} in this deck.')

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return self.name

    def display_hand(self):
        '''Shows cards in hand to player'''
        print(f"{self.name}'s hand is: ")
        for card in self.hand:
            print(card)

        

    def calculate_hand_value(self):
        '''return the total value of the hand'''
        card_total = self.hand.card.value


class Dealer(Player):
    def __init__(self):
        self.name = 'Dealer'
        super().__init__('Dealer')


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player(name=input("What is your name? "))
        self.dealer = Dealer()
        self.deal_cards()
        self.player.display_hand()
        self.dealer.display_hand()
        self.hit(self.player)



    def deal_cards(self):
        '''Deal 2 cards each to the player and the dealer '''
        while len(self.player.hand) < 2 and len(self.dealer.hand) < 2:
            card = self.deck.cards.pop()
            self.player.hand.append(card)
            card = self.deck.cards.pop()
            self.dealer.hand.append(card)
        print(f'{self.player} has {self.player.hand} \n'
              f'and {self.dealer} has {self.dealer.hand}')

    def hit(self, player):
        '''Deal one card to the selected player'''
        hit_or_stay = input("Hit or stay? Enter H or S: ").lower()
        #While the value is < 21, then we want to H or S
        if hit_or_stay == 'h':
            card = self.deck.cards.pop()
            self.player.hand.append(card)
            print(card)
        else:
            print('Player does not want a card')
            #We are trying to get the game to do nothing and continue the game is S is submitted
            


# print(ace_of_spades)
# print(four_of_clubs)


new_game = Game()
# TODO Add values of each hand so player and dealer can decide to hit or stay