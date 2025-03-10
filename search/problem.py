class Problem:
    def __init__(self, initial_state, goal_state, streets):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.streets = streets

    def successors(self, state):
        actions = self.actions(state)
        return [(self.results(state, action), action) for action in actions]

    def actions(self, state):
        return self.streets[state].keys()

    def results(self, state, action):
        return action

    def cost(self, state, action):
        return self.streets[state][action]

    def goal_test(self, state):
        return self.goal_state == state
