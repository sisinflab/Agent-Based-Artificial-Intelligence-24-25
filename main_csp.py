from csp.csp import CSP
from csp.backtrack import Backtracking, BacktrackingFC
from csp.heuristics import *
from csp.arc_consistency import AC3


class DifferentValues:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def check(self, assignment):
        value1 = assignment.get(self.var1)
        value2 = assignment.get(self.var2)
        if value1 and value2:
            return value1 != value2
        return True


variables = ['WA', 'NT', 'Q', 'NSW', 'V', 'SA', 'T']
domain = ['red', 'green', 'blue']
domains = {variable: domain for variable in variables}
constraints = [
    DifferentValues('SA', 'WA'),
    DifferentValues('SA', 'NT'),
    DifferentValues('SA', 'Q'),
    DifferentValues('SA', 'NSW'),
    DifferentValues('SA', 'V'),
    DifferentValues('WA', 'NT'),
    DifferentValues('NT', 'Q'),
    DifferentValues('Q', 'NSW'),
    DifferentValues('NSW', 'V')
]


problem = CSP(variables=variables, domains=domains, constraints=constraints)

search = Backtracking(problem, variable_criterion=random_variable, value_criterion=unordered_value)
#print(search.run())

search = Backtracking(problem, variable_criterion=minimum_remaining_values, value_criterion=unordered_value)
#print(search.run())

search = Backtracking(problem, variable_criterion=degree_heuristic, value_criterion=unordered_value)
#print(search.run())

search = BacktrackingFC(problem, variable_criterion=random_variable, value_criterion=unordered_value)
#print(search.run())

ac3 = AC3(problem)

print(ac3.run())
print(ac3.csp.domains)