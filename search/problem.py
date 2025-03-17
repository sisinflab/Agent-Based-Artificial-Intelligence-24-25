import math
import copy


class Problem:
    def __init__(self, initial_state, goal_state=None):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def successors(self, state):
        pass

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def goal_test(self, state):
        if isinstance(self.goal_state, list):
            return state in self.goal_state
        else:
            return state == self.goal_state

    def cost(self, state, action):
        return 1

    def heuristic(self, state):
        pass


class StreetsProblem:
    def __init__(self, initial_state, goal_state, streets, coords=None):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.streets = streets
        self.coords = coords

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

    def heuristic(self, state):
        x_current, y_current = self.coords[state]
        x_goal, y_goal = self.coords[self.goal_state]

        return math.sqrt((x_current - x_goal) ** 2 + (y_current - y_goal) ** 2)


class EightProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def successors(self, state):
        actions = self.actions(state)
        return [(self.result(state, action), action) for action in actions]

    def result(self, state, action):
        new_state = copy.deepcopy(state)
        index = new_state.index(0)
        row = index // 3
        col = index % 3

        new_row, new_col = row, col

        if action == 'up':
            new_row -= 1
        if action == 'down':
            new_row += 1
        if action == 'left':
            new_col -= 1
        if action == 'right':
            new_col += 1

        new_index = new_row * 3 + new_col

        new_state[new_index], new_state[index] = state[index], state[new_index]

        return new_state

    def actions(self, state):
        index = state.index(0)
        row = index // 3
        col = index % 3

        actions = ['up', 'down', 'left', 'right']

        if row < 1:
            actions.remove('up')
        if row >= 2:
            actions.remove('down')
        if col < 1:
            actions.remove('left')
        if col >= 2:
            actions.remove('right')

        return actions

    def goal_test(self, state):
        return self.goal_state == state

    def cost(self, state, action):
        return 1

    """
    def heuristic(self, state):
        # number of misplaced tiles
        return sum([x != y for x, y in zip(state, self.goal_state) if x != 0])

    """

    def heuristic(self, state):
        # total manhattan distance
        distance = 0
        for tile in range(1, 9):
            current_index = state.index(tile)
            current_row = current_index // 3
            current_col = current_index % 3
            goal_index = self.goal_state.index(tile)
            goal_row = goal_index // 3
            goal_col = goal_index % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)

        return distance
