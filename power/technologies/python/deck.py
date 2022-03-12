"""
@author: acfromspace
"""

import random

# A card has a value and suit.
# `show()` which prints the value and suit of said card.
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))

# A deck is a list of cards.
# `build()` us where it initially builds itself.
# `shuffle()` has the power to shuffle randomly.
# `drawCard()` removes the top card by popping from the deck.
# `show()` shows each card left in the deck.
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Clubs", "Spades", "Hearts", "Diamonds"]:
            # for value in range(1, 14):
            for value in ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]:
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

# A player has a hand and name.
# `draw()` gives a user a card from the deck.
# `showHand()` shows the card(s) within the user object.
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

    def throwAway(self):
        return self.hand.pop()


# Create a deck, shuffle the cards, and show the cards.
deck = Deck()
deck.shuffle()
deck.show()

# Create a player to draw a card from the deck and show their card(s).
ac = Player("AC")
ac.draw(deck)
ac.showHand()
