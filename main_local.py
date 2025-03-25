from search.problem import EightQueenProblem
from search.local_search import HillClimbingSearch, SimulatedAnnealingSearch, GeneticAlgorithm
import random

def scheduler(time):
    initial_temp = 1000
    lamb = 0.001
    return initial_temp - lamb * time


initial = [random.randint(0, 7) for _ in range(8)]
problem = EightQueenProblem(initial)
# search = GeneticAlgorithm(problem=problem, population_size=100, max_generation=1000, state_len=8, gene_pool=[0, 1, 2, 3, 4, 5, 6, 7], mutation_rate=0.1)
search = SimulatedAnnealingSearch(problem=problem, schedule=scheduler, max_time=10000000)
print(search.run())
