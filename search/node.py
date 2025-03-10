class Node:
    def __init__(self, parent, action, depth, cost, state):
        self.parent = parent
        self.action = action
        self.depth = depth
        self.cost = cost
        self.state = state

    def __repr__(self):
        return str(self.state)

    def expand(self, problem):
        successors = []
        for state, action in problem.successors(self.state):
            successors += [Node(self, action, self.depth+1, self.cost+problem.cost(self.state, action), state)]
        return successors

    def solution(self):
        path = []
        node = self

        while node.parent is not None:
            path.append(node.action)
            node = node.parent

        return path[::-1]

