import random
import copy
from tree.tree import Tree

def should_mutate(mutation_rate=0.1) -> bool:
    return random.random() <= mutation_rate

def mutate(individual: Tree, max_height=3) -> Tree:
    mutant = copy.deepcopy(individual)
    node = mutant.random_node()
    new_subtree = Tree()
    new_subtree.grow(max_height)
    node.value = new_subtree.root.value
    node.left = new_subtree.root.left
    node.right = new_subtree.root.right
    return mutant

def run_mutations(children: list[Tree], mutation_rate=0.1) -> list[Tree]:
    mutated = []
    for child in children:
        if should_mutate(mutation_rate):
            mutated.append(mutate(child))
        else:
            mutated.append(child)
    return mutated
