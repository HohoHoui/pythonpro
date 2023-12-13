class Card:
    """A playing card."""
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        replay = self.rank + self.suit
        return replay

class Unprintable_Card(Card):
    def __str__(self):
        return "<unprintable>"

class Positionable_Card(Card):
    def __init__(self, rank, suit, face_up = True):
        super().__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            replay = super().__str__()
        else:
            replay = "XX"
        return replay
    
    def flip(self):
        self.is_face_up = not self.is_face_up

class BJ_Crad:
	face_up : False
class Hand:
    """A hand of playing cards."""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            replay = ""
            for card in self.cards:
                replay += str(card) + " "
        else:
            replay = "<empty>"
        return replay

    def clear(self):
    	self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

#class Deck:
	#def populate():
	#def shuffle():
#class Player:
	#def add():
	
#class Dealer:
	#def add():

#class BJ_Game:

print("\t\tWelcome to Blackjack!\n")
per_num = int(input("How many players? <1 - 7>: "))

for i in range(per_num):
	name = input("Enter player name: ")

card1 = Card(rank = "A", suit = "c")
card2 = Unprintable_Card(rank = "A", suit = "d")
card3 = Positionable_Card(rank = "A", suit = "h")

print("Printing the rest of the objects individually:")
print(card1)

print("\nPrinting a Positionable_Card object:")
print(card2)

print("\nPrinting a Positionable_Card object:")
print(card3)

print("\nFliping the Positionable_Card object.")
card3.flip()
print("Printing the Positionable_Card object:")
print(card3)

#<define Card class>
#<define Hand class>
#<define Unprintable_Card class>
#<define Positionable_Card class>

if __name__ == "__main__":
	print ("You ran module but must 'import' it.")
	input("\n\nPress the enter key to exit.")
	
"""
print("\nPrinting my hand before I add any cards:")
my_hand = Hand()
print(my_hand)
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nPrinting my hand after adding 5 cards:")
print(my_hand)

print("\nGave the first two cards from my hand to your hand.")
your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("Your hand:")
print(your_hand)
print("My hand:")
print(my_hand)
my_hand.clear()
print("\nMy hand after clearing it:")
print(my_hand)
"""

