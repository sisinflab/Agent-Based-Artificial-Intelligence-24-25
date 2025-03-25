from search.node import Node
import random
import math


class HillClimbingSearch:
    def __init__(self, problem):
        self.problem = problem

    def run(self):
        current = Node(state=self.problem.initial_state, parent=None, cost=0, depth=0, action=None)

        while True:
            neighbors = current.expand(self.problem)
            best = min(neighbors, key=lambda n: self.problem.heuristic(n.state))

            if self.problem.heuristic(best.state) >= self.problem.heuristic(current.state):
                return current, self.problem.heuristic(current.state)

            current = best


class SimulatedAnnealingSearch:
    def __init__(self, problem, max_time, schedule):
        self.problem = problem
        self.max_time = max_time
        self.schedule = schedule

    def run(self):
        current = Node(state=self.problem.initial_state, parent=None, depth=0, action=None, cost=0)

        for time in range(self.max_time):
            temp = self.schedule(time)

            if temp == 0:
                return current

            neighbor = random.choice(current.expand(self.problem))

            delta = self.problem.heuristic(current.state) - self.problem.heuristic(neighbor.state)

            if delta > 0 or random.uniform(0, 1) < math.exp(delta/temp):
                current = neighbor

        return current, self.problem.heuristic(current.state)


class GeneticAlgorithm:
    def __init__(self, problem, population_size, max_generation, state_len, gene_pool, mutation_rate):
        self.problem = problem
        self.gene_pool = gene_pool
        self.mutation_rate = mutation_rate
        self.population_size = population_size
        self.state_len = state_len
        self.max_generation = max_generation

    def select(self, population):
        fitness = [self.problem.value(individual) for individual in population]
        probability = [fitness / sum(fitness) for fitness in fitness]
        return random.choices(population, weights=probability, k=2)

    def crossover(self, parent1, parent2):
        c_point = random.randint(0, self.state_len)
        return parent1[:c_point] + parent2[c_point:]

    def mutation(self, individual):
        if random.uniform(0, 1) < self.mutation_rate:
            pos = random.choice(range(self.state_len))
            individual[pos] = random.choice(self.gene_pool)
        return individual

    def run(self):
        population = [random.choices(self.gene_pool, k=self.state_len) for _ in range(self.population_size)]
        best = None

        for _ in range(self.max_generation):
            population = [self.mutation(self.crossover(*self.select(population))) for _ in range(self.population_size)]
            best = max(population, key=self.problem.value)
            if self.problem.goal_test(best):
                break

        return best, self.problem.value(best)