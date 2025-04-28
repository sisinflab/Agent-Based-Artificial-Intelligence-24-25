import numpy as np


class Minimax:
    def __init__(self, game):
        self.game = game

    def minimax_decision(self, state):
        return max(self.game.actions(state),
                   key=lambda a: self.min_value(self.game.result(state, a)))

    def min_value(self, state):
        if self.game.terminal_test(state):
            return self.game.utility(state)

        v = np.inf

        for s, a in self.game.successors(state):
            v = min(v, self.max_value(s))
        return v

    def max_value(self, state):
        if self.game.terminal_test(state):
            return self.game.utility(state)

        v = - np.inf

        for s, a in self.game.successors(state):
            v = max(v, self.min_value(s))
        return v

    def run(self):
        moves = []
        state = self.game.initial

        while True:
            if self.game.terminal_test(state):
                return moves

            action = self.minimax_decision(state)
            state = self.game.result(state, action)
            moves.append((self.game.player, action))
            self.game.next_player()
