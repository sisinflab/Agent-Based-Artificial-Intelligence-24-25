from search.node import Node


class TreeSearch:
    def __init__(self, problem, strategy):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []

    def run(self):
        self.fringe.append(Node(None, None, depth=0, cost=0, state=self.problem.initial_state))

        while True:
            if len(self.fringe) == 0:
                return 'fail', []

            self.fringe, node = self.strategy.select(self.fringe)

            if self.problem.goal_test(node.state):
                return 'success', node.solution()

            self.fringe += node.expand(self.problem)
