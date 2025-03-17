from search.problem import StreetsProblem, EightProblem
from search.tree_search import TreeSearch
from search.graph_search import GraphSearch
from search.strategy import *


streets = {
    'Andria': {'Corato': 3, 'Trani': 2},
    'Corato': {'Andria': 3, 'Ruvo': 2, 'Trani': 3, 'Altamura': 4},
    'Altamura': {'Corato': 4, 'Ruvo': 3, 'Modugno': 5},
    'Ruvo': {'Corato': 2, 'Bisceglie': 3, 'Terlizzi': 2, 'Altamura': 3},
    'Terlizzi': {'Ruvo': 2, 'Molfetta': 2, 'Bitonto': 2},
    'Bisceglie': {'Trani': 2, 'Ruvo': 3, 'Molfetta': 2},
    'Trani': {'Andria': 2, 'Corato': 3, 'Bisceglie': 2},
    'Molfetta': {'Bisceglie': 2, 'Giovinazzo': 2, 'Terlizzi': 2},
    'Giovinazzo': {'Molfetta': 2, 'Modugno': 3, 'Bari': 2, 'Bitonto': 3},
    'Bitonto': {'Modugno': 3, 'Giovinazzo': 3, 'Terlizzi': 2},
    'Modugno': {'Bitonto': 3, 'Giovinazzo': 3, 'Bari': 2, 'Altamura': 5, 'Bitetto': 1},
    'Bari': {'Modugno': 2, 'Giovinazzo': 2, 'Bitetto': 2},
    'Bitetto': {'Bari': 2, 'Modugno': 1}
}

cities_coords = {
    'Andria': (41.2316, 16.2917),
    'Corato': (41.1465, 16.4147),
    'Altamura': (40.8302, 16.5545),
    'Ruvo': (41.1146, 16.4886),
    'Terlizzi': (41.1321, 16.5461),
    'Bisceglie': (41.243, 16.5052),
    'Trani': (41.2737, 16.4162),
    'Molfetta': (41.2012, 16.5983),
    'Giovinazzo': (41.1874, 16.6682),
    'Bitonto': (41.1118, 16.6902),
    'Modugno': (41.0984, 16.7788),
    'Bari': (41.1187, 16.852),
    'Bitetto': (41.040, 16.748)
}

# problem = StreetsProblem(initial_state='Bitetto', goal_state='Trani', streets=streets, coords=cities_coords)
problem = EightProblem([1, 2, 3, 4, 0, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 0])
search = GraphSearch(problem, GreedySearch(problem))
print(search.run())
