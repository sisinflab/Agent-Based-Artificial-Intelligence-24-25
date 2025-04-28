class Game:
    def __init__(self, initial, terminal, environment):
        self.initial = initial
        self.terminal = terminal
        self.environment = environment
        self.player = 'MAX'

    def actions(self, state):
        return self.environment[state].keys()

    def successors(self, state):
        actions = self.actions(state)
        return [(self.result(state, action), action) for action in actions]

    def result(self, state, action):
        return self.environment[state][action]

    def terminal_test(self, state):
        return state in self.terminal.keys()

    def utility(self, state):
        if self.player == 'MAX':
            return self.terminal[state]
        elif self.player == 'MIN':
            return - self.terminal[state]

    def next_player(self):
        if self.player == 'MAX':
            self.player = 'MIN'
        elif self.player == 'MIN':
            self.player = 'MAX'


class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.initial = [' '] * (size * size)
        self.player = 'X'

    def actions(self, state):
        return [i for i, cell in enumerate(state) if cell == ' ']

    def successors(self, state):
        actions = self.actions(state)
        return [(self.result(state, action), action) for action in actions]

    def result(self, state, action):
        new_state = state.copy()
        new_state[action] = self.player
        return new_state

    def check_winner(self, state):

        for i in range(0, len(state), self.size + 1):
            row = state[i: i+self.size]
            if ' ' not in row and len(set(row)) == 1:
                return row[0]

        for i in range(self.size):
            col = [state[row * self.size + i] for row in range(self.size)]
            if ' ' not in col and len(set(col)) == 1:
                return col[0]

        diag = state[0: self.size**2: self.size]
        if ' ' not in diag and len(set(diag)) == 1:
            return diag[0]

        anti_diag = state[self.size-1: self.size**2 - 1: self.size - 1]
        if ' ' not in anti_diag and len(set(anti_diag)) == 1:
            return anti_diag[0]

        return None

    def terminal_test(self, state):
        return self.check_winner(state) and ' ' not in state

    def utility(self, state):
        if self.terminal_test(state):
            if self.player == 'X':
                return 1
            elif self.player == 'O':
                return -1
        return 0

    def next_player(self):
        if self.player == 'X':
            self.player = 'O'
        elif self.player == 'O':
            self.player = 'X'
