from search.problem import EightQueenProblem
from search.local_search import HillClimbingSearch, SimulatedAnnealingSearch, GeneticAlgorithm
import random

def scheduler(time):
    initial_temp = 1000
    lamb = 0.001
    return initial_temp - lamb * time


initial = [random.randint(0, 7) for _ in range(8)]
problem = EightQueenProblem(initial)


it = 0
while True:
    it+=1
    search = HillClimbingSearch(problem=EightQueenProblem([random.randint(0, 7) for _ in range(8)]))
    result = search.run()
    if result[1] == 0:
        print(f"Found Solution {result[0].state}, with cost {result[1]}, after {it} iterations.")
        break