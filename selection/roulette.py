import random
from tree.tree import Tree

def roulette_wheel_selection(population: list, fitnesses: list) -> Tree:
    total_fitness = sum(fitnesses)
    if total_fitness == 0:
        return random.choice(population)
    selection_probs = [f / total_fitness for f in fitnesses]
    r = random.random()
    cumulative = 0
    for individual, prob in zip(population, selection_probs):
        cumulative += prob
        if r <= cumulative:
            return individual
    return population[-1]
