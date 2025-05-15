import copy


class Backtracking:
    def __init__(self, csp, variable_criterion, value_criterion):
        self.csp = csp
        self.variable_criterion = variable_criterion
        self.value_criterion = value_criterion

    def backtrack_search(self, assignment):
        if self.csp.complete(assignment) and self.csp.consistent(assignment):
            return assignment

        variable = self.variable_criterion(self.csp, assignment)

        for value in self.value_criterion(self.csp, variable):
            self.csp.assign(assignment, value=value, variable=variable)

            if self.csp.consistent(assignment):
                result = self.backtrack_search(assignment)

                if result:
                    return result

            self.csp.unassign(assignment, variable=variable)

        return False

    def run(self):
        return self.backtrack_search(assignment={})


class BacktrackingFC:
    def __init__(self, csp, variable_criterion, value_criterion):
        self.csp = csp
        self.variable_criterion = variable_criterion
        self.value_criterion = value_criterion

    def forward_check(self, assignment, variable):
        new_domains = copy.deepcopy(self.csp.domains)

        for var in self.csp.variables:
            new_assignment = copy.deepcopy(assignment)
            if var not in new_assignment and var in self.csp.neighbours.get(variable, []):
                for value in new_domains[var][:]:
                    self.csp.assign(new_assignment, var, value)
                    if not self.csp.consistent(new_assignment):
                        new_domains[var] = [v for v in new_domains[var] if v != value]

                if len(new_domains[var]) == 0:
                    return False
        return new_domains

    def backtrack_search(self, assignment):
        if self.csp.complete(assignment) and self.csp.consistent(assignment):
            return assignment

        variable = self.variable_criterion(self.csp, assignment)

        for value in self.value_criterion(self.csp, variable):
            self.csp.assign(assignment, value=value, variable=variable)

            old_domains = copy.deepcopy(self.csp.domains)
            new_domains = self.forward_check(assignment, variable)

            if new_domains and self.csp.consistent(assignment):
                self.csp.domains = new_domains
                result = self.backtrack_search(assignment)

                if result:
                    return result

            self.csp.domains = old_domains
            self.csp.unassign(assignment, variable=variable)

        return False

    def run(self):
        return self.backtrack_search(assignment={})