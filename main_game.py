from game.game import Game, TicTacToe
from game.minimax import Minimax
from game.alphabeta import AlphaBeta

dummy_environment = {
    'A': {'a1': 'B', 'a2': 'C', 'a3': 'D'},
    'B': {'b1': 'E', 'b2': 'F', 'b3': 'G'},
    'C': {'c1': 'H', 'c2': 'I', 'c3': 'L'},
    'D': {'d1': 'M', 'd2': 'N', 'd3': 'O'},
}

terminal_state = {
    'E': 3,
    'F': 12,
    'G': 8,
    'H': 2,
    'I': 4,
    'L': 6,
    'M': 14,
    'N': 5,
    'O': 2
}


game = Game(initial='A', environment=dummy_environment, terminal=terminal_state)
# game = TicTacToe(size=3)
search = AlphaBeta(game)
print(search.run())
