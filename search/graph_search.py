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
                self.closed += [node.state]

                fringe_states = [n.state for n in self.fringe]
                self.fringe += [new_node for new_node in node.expand(self.problem) if
                                new_node.state not in fringe_states]
