from random import shuffle

class Card:
    
    """ A class representing a card from the deck

    Properties:
    suit (string): The suit/house of the card: "Clubs", "Diamonds", "Hearts", or "Spades"
    value (integer): The point value of the card
    name (string): The name of the card: numerical corresponding name for basic numerical cards, and "Jack", "Queen", "King", or "Ace" with values of 11-14 """

    def __init__(self, value, suit):
        
        """ Initialize a new card and looks at the value and suit of it

        Args:
        value (integer): The point value of the card
        suit (string): The suit/house of the card: "Clubs", "Diamonds", "Hearts", or "Spades" """

        self.value = value
        self.suit = suit
        value_names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
        self.name = value_names.get(value, str(value))

    def __str__(self):
        
        """ Return a string description of the name and suit of the card

        Returns:
        string: A string in the format "(title) of (house)" """

        return f"{self.name} of {self.suit}"


class Deck:
    
    """ A class for a deck of 52 cards

    Properties:
    cards (list): A list of cards that represents the deck """

    def __init__(self):
        
        """ Created new deck of 52 cards. Shuffles the deck """

        self.cards = [Card(value, suit) for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]
                      for value in range(2, 15)]
        shuffle(self.cards)

    def draw(self):
        
        """ Draws a card

        Returns:
        Card: Whatever the chosen card is
        
        Brings up:
        RuntimeError: Only if there are not more cards """

        if self.cards:
            return self.cards.pop()
        else:
            raise RuntimeError("No more cards")
