import random

def random_variable(csp, assignment):
    return random.choice([var for var in csp.variables if var not in assignment.keys()])

def unordered_value(csp, variable):
    return csp.domains[variable]

def minimum_remaining_values(csp, assignment):
    unassigned = [var for var in csp.variables if var not in assignment.keys()]
    return min(unassigned, key = lambda v: len(csp.domains[v]))


def degree_heuristic(csp, assignment):
    unassigned = [var for var in csp.variables if var not in assignment.keys()]
    constraints_count = {v:0 for v in unassigned}

    for c in csp.constraints:
        if c.var1 in unassigned and c.var2 in unassigned:
            constraints_count[c.var1] += 1
            constraints_count[c.var2] += 1

    return max(unassigned, key = lambda v: constraints_count[v])