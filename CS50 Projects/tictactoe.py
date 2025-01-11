""" A tic tac toe game. """

# standard modules
from argparse import ArgumentParser
import sys

# modules specific to this program
# tictactoe.py
from logging_board import LoggingBoard as Board
from player import HumanPlayer, ComputerPlayer


class TicTacToe:
    """ A tic tac toe game. Can be played by any humans and/or
    computers.
    
    Attributes:
        players (list of Player): the two players
        board (Board): the tic tac toe Board
        score (dict of Player: int): the players' scores
    """
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.score = {p: 0 for p in self.players}
        
    def reset_game(self):
        """ Switch the player's letters and order and get a new board. """
        self.board = Board()
        self.players.reverse()
        self.players[0].set_letter("x")
        self.players[1].set_letter("o")
        
    def play_round(self):
        """ Play one round of tic tac toe. """
        turn = 0
        while not self.board.game_over():
            player = self.players[turn % 2]
            player.take_turn(self.board)
            turn += 1

    def play_game(self):
        """ Play multiple rounds of tic tac toe. """
        while True:
            self.reset_game()
            for p in self.players:
                print(f"{p.name} is playing as {p.letter}")
            print()
            self.play_round()
            print()
            winner = self.board.get_winner()
            if winner:
                print(f"{winner.name} wins!")
                self.score[winner] += 1
            else:
                print("Tie game")
            for p in self.players:
                print(f"{p.name} has {self.score[p]} points")
            print()
            while True:
                playagain = input("Play again? (y/n): ")
                if playagain == "n":
                    return
                elif playagain == "y":
                    break
                print("Please type 'y' or 'n'")


def parse_args(arglist):
    """ Parse command line arguments. """
    parser = ArgumentParser()
    parser.add_argument("player1_name", help="Player 1 name (or 'computer')")
    parser.add_argument("player2_name", help="Player 2 name (or 'computer')")
    args = parser.parse_args(arglist)
    return args


def main(arglist):
    """ Create two Player objects and start a game of tic tac toe. """
    args = parse_args(arglist)
    p1 = (ComputerPlayer("Rosie the Robot") if args.player1_name == "computer"
          else HumanPlayer(args.player1_name))
    p2 = (ComputerPlayer("Roger the Robot") if args.player2_name == "computer"
          else HumanPlayer(args.player2_name))
    game = TicTacToe(p1, p2)
    game.play_game()


if __name__ == "__main__":
    main(sys.argv[1:])
