import random
import copy
from tree.tree import Tree
	
def mutate(individual: Tree, max_height=3, mutation_rate=0.1) -> Tree:
    if random.random() > mutation_rate:
        return individual
    mutant = copy.deepcopy(individual)
    # needs to change to be a prob per node to be mutated 
    # rather than prob of overall tree
    node = mutant.random_node()
    new_subtree = Tree()
    new_subtree.grow(max_height)
    node.value = new_subtree.root.value
    node.left = new_subtree.root.left
    node.right = new_subtree.root.right
    return mutant
