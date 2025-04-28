import numpy as np


class AlphaBeta:
    def __init__(self, game):
        self.game = game

    def alphabeta_decision(self, state):
        return max(self.game.actions(state),
                   key=lambda a: self.min_value(self.game.result(state, a), -np.inf, np.inf))

    def min_value(self, state, alpha, beta):
        if self.game.terminal_test(state):
            return self.game.utility(state)

        v = np.inf

        for s, a in self.game.successors(state):
            v = min(v, self.max_value(s, alpha, beta))
            if v <= alpha:
                return v
            beta = min(v, beta)

        return v

    def max_value(self, state, alpha, beta):
        if self.game.terminal_test(state):
            return self.game.utility(state)

        v = - np.inf

        for s, a in self.game.successors(state):
            v = max(v, self.min_value(s, alpha, beta))
            if v >= beta:
                return v
            alpha = max(v, alpha)
        return v

    def run(self):
        moves = []
        state = self.game.initial

        while True:
            if self.game.terminal_test(state):
                return moves

            action = self.alphabeta_decision(state)
            state = self.game.result(state, action)
            moves.append((self.game.player, action))
            self.game.next_player()
