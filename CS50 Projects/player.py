""" Human and computer tic tac toe players. """


import random

from claimed_square_error import ClaimedSquareError


class Player:
    """ Abstract base class for tic tac toe players.
    
    Attributes:
        name (str): the player's name
        letter (str): the player's current letter ('x' or 'o')
    """
    def __init__(self, name):
        self.name = name
        self.letter = ' '
    
    def set_letter(self, letter):
        """ Set the player's current letter """
        self.letter = letter
    
    def take_turn(self, board):
        """ Claim one of the available squares on the board.

        Args:
            board (Board): a tic tac toe board.
        
        Side effects:
            Claims a square on the board.
        """
        raise NotImplementedError


class ComputerPlayer(Player):
    """ A computer tic tac toe player. Chooses its moves at random. """
    def take_turn(self, board):
        """ Randomly select an available square.
        
        Args:
            board (Board): a tic tac toe board.
        
        Side effects:
            Claims a square on the board.
        """
        available = board.get_unclaimed_squares()
        choice = random.choice(available)
        board.claim_square(self, choice)


class BetterComputerPlayer(ComputerPlayer):
    """ A computer tic tac toe player with a more sophisticated strategy
    than ComputerPlayer."""
    def take_turn(self, board):
        """ Select the middle square if available; otherwise, select
        a square at random.
        
        Args:
            board (Board): a tic tac toe board.
        
        Side effects:
            Claims a square on the board.
        """
        if board.is_unclaimed(4):
            board.claim_square(4)
        else:
            #ComputerPlayer.take_turn(self, board)
            super().take_turn(board)


class HumanPlayer(Player):
    """ A human tic tac toe player. Looks and the board and makes a
    (hopefully) intelligent decision about where to play.
    """
    def take_turn(self, board):
        """ Ask the user to choose an available square on the board.
        
        Args:
            board (Board): a tic tac toe board.
        
        Side effects:
            Claims a square on the board.
        """
        while True:
            print(board)
            choice = input(f"{self.name}'s turn; choose"
                           f" an open square for {self.letter}: ")
            print()
            try:
                index = int(choice)
            except ValueError:
                print("Please enter a number")
                continue
            
            try:
                board.claim_square(self, index)
            except RuntimeError:
                print("That square is already taken; choose another one")
            except ValueError:
                print("Please enter a number between 0 and 8")
            except ClaimedSquareError:
                print("That square is already taken; choose another one")
            else:
                return
