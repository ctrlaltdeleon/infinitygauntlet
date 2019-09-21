"""
@author: acfromspace
"""

import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Clubs", "Spades", "Hearts", "Diamonds"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle(self):
        # Goes through values of 51 to 1 (range stops right before the value).
        for index in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, index)
            self.cards[index], self.cards[r] = self.cards[r], self.cards[index]

    def drawCard(self):
        return self.cards.pop()

    def show(self):
        for card in self.cards:
            card.show()


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()


# Create a deck and shuffle the cards.
deck = Deck()
deck.shuffle()

# Create a player to draw a card from the deck and show the cards.
ac = Player("AC")
ac.draw(deck)
ac.showHand()
