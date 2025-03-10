from search.node import Node


class GraphSearch:
    def __init__(self, problem, strategy):
        self.problem = problem
        self.strategy = strategy
        self.fringe = []
        self.closed = []

    def run(self):
        self.fringe.append(Node(None, None, depth=0, cost=0, state=self.problem.initial_state))

        while True:
            if len(self.fringe) == 0:
                return 'fail', []

            self.fringe, node = self.strategy.select(self.fringe)
            if not node:
                return 'fail', []

            if self.problem.goal_test(node.state):
                return 'success', node.solution()

            if node.state not in self.closed:
                self.closed.append(node.state)
                self.fringe += node.expand(self.problem)
