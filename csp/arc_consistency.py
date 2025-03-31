class AC3:
    def __init__(self, csp):
        self.csp = csp
        self.queue = self.arcs()


    def arcs(self):
        queue = []

        for var in self.csp.neighbours.keys():
            queue += [(var, neighbour) for neighbour in self.csp.neighbours[var]]

        return queue

    def remove_inconsistent_values(self, var1, var2):
        removed = False
        for value1 in self.csp.domains[var1][:]:
            constrains_results = [self.csp.consistent({var1: value1, var2: value2}) for value2 in self.csp.domains[var2]] #for constraint in self.csp.constraints if constraint.var1 == var1 and constraint.var2 == var2]
            if not any(constrains_results):
                self.csp.domains[var1].remove(value1)
                removed = True

        return removed

    def run(self):
        while len(self.queue)>0:
            var1, var2 = self.queue.pop(0)

            if self.remove_inconsistent_values(var1, var2):

                if len(self.csp.domains[var1]) == 0:
                    return False

                for var_n in self.csp.neighbours[var1]:
                    if var_n != var2:
                        self.queue.append((var_n, var1))

        return True