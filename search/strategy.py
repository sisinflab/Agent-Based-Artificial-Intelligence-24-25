from random import shuffle


class RandomSearch:
    def select(self, fringe):
        shuffle(fringe)
        return fringe, fringe.pop(0)


class BreadthFirstSearch:
    def select(self, fringe):
        return fringe, fringe.pop(0)


class UniformCostSearch:
    def select(self, fringe):
        fringe = sorted(fringe, key=lambda n: n.cost)
        return fringe, fringe.pop(0)


class DepthFirstSearch:
    def select(self, fringe):
        return fringe, fringe.pop()


class DepthLimitedSearch:
    def __init__(self, limit):
        self.limit = limit
    def select(self, fringe):
        node = fringe.pop()
        if node.depth <= self.limit:
            return fringe, node
        return None, None


class GreedySearch:
    def __init__(self, problem):
        self.problem = problem

    def select(self, fringe):
        fringe = sorted(fringe, key=lambda n: self.problem.heuristic(n.state))
        return fringe, fringe.pop(0)


class AStarSearch:
    def __init__(self, problem):
        self.problem = problem

    def select(self, fringe):
        fringe = sorted(fringe, key=lambda n: n.cost + self.problem.heuristic(n.state))
        return fringe, fringe.pop(0)

