import random

class MinConflict:
    def __init__(self, csp, max_steps):
        self.csp = csp
        self.max_steps = max_steps

    def n_conflicts(self, current, variable, value):
        count = 0
        for constraint in self.csp.constraints:
            if (variable in {constraint.var1, constraint.var2} and
                    not constraint.check({**current, variable: value})):
                count += 1
        return count

    def run(self):
        current = {var: random.choice(self.csp.domains[var]) for var in self.csp.variables}

        for step in range(self.max_steps):
            if self.csp.consistent(current):
                return current

            variable = random.choice([var for var in self.csp.variables
                                      if self.n_conflicts(current, var, current[var]) > 0])

            value = min(self.csp.domains[variable],
                        key=lambda val: self.n_conflicts(current, variable, val))

            current[variable] = value

        return False

