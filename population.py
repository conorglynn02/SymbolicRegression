import random
from tree.tree import Tree

def make_population(size: int, max_tree_height: int) -> list:
    population = []
    for _ in range(size):
        tree = Tree()
        random_height = random.randint(1, max_tree_height)
        # half grow and half full
        if _ % 2 == 0:
            # grow method
            tree.grow(max_height=random_height)
        else:
            # full method
            tree.full(max_height=random_height)
        population.append(tree)
    return population
