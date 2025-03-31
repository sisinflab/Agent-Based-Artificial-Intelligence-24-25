import csp.csp


class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.neighbours = self.compute_neighbours()

    def compute_neighbours(self):
        neighbours = {}
        for c in self.constraints:
            neighbours.setdefault(c.var1, []).append(c.var2)
            neighbours.setdefault(c.var2, []).append(c.var1)
        return neighbours


    def consistent(self, assignment):
        return all(constraint.check(assignment) for constraint in self.constraints)

    def complete(self, assignment):
        return len(assignment) == len(self.variables)

    def assign(self, assignment, variable, value):
        assignment[variable] = value
        return assignment

    def unassign(self, assignment, variable):
        assignment.pop(variable)
        return assignment
