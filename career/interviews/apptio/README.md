# APPTIO

## Round 1 (Online)

**Environment:** 30 minutes with no person.

**Type:** Behavioral and technical.

**Notes:**

- CCAT assessment.

## Round 2 (Phone)

**Environment:** 20 minutes with Recruiter.

**Type:** Behavioral.

**Notes:**

- "What do you want from working here?"
- "Are you open to relocation?"
- "Show your eagerness to learn!"

## Round 3 (Online & Phone)

**Environment:** 1 hour with Vice President of Engineering.

**Type:** Behavioral and technical.

**Notes:**

- "What have you been doing the past year?"
- "Can you reverse a string without any shortcuts?"

```py
def reverseString(string):
    solution = ""
    for character in string[::-1]:
        solution += character
    return solution

def reverseRecursion(string):
    return string if len(string) <= 1 else reverseRecursion(string[1:]) + string[0]

"""
Output:

reverseRecursion(hello)
    = reverseRecursion(ello) + h           # The recursive step
    = reverseRecursion(llo) + e + h
    = reverseRecursion(lo) + l + e + h
    = reverseRecursion(o) + l + l + e + h  # Base case
    = o + l + l + e + h
    = olleh
"""
```

- "Can you do an iterative solution to a factorial function?"

```py
def factorial(number):
    solution = 1
    for index in range(1,number+1):
        solution *= index
    return solution
```

- "Can you do a recursive solution to a factorial function?"

```py
def factorialRecursion(number):
    return number if number <= 1 else number * factorialRecursion(number-1)
```

- "Can you make an object oriented design for a deck of cards?"

```py
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

class Game:
    def __init__(self, game):
        self.game = game

# Create a deck and shuffle the cards.
deck = Deck()
deck.shuffle()

# Create a player to draw a card from the deck and show the cards.
ac = Player("AC")
ac.draw(deck)
ac.showHand()
```

## Round 4 (On site)

**Environment:** ?

**Type:** ?

**Notes:**

- Did not make it.
