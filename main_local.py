from search.problem import EightQueenProblem
from search.local_search import HillClimbingSearch, SimulatedAnnealingSearch, GeneticAlgorithm
import random

initial = [random.randint(0, 7) for _ in range(8)]
problem = EightQueenProblem(initial)
search = GeneticAlgorithm(problem=problem, population_size=100, max_generation=100, state_len=8, gene_pool=[0, 1, 2, 3, 4, 5, 6, 7], mutation_rate=0.3)
print(search.run())
