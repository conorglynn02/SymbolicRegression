import random
import copy
from tree.tree import Tree

def roulette_wheel_selection(population, fitnesses):
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


def collect_nodes(node):
    if node is None:
        return []
    nodes = [node]
    nodes += collect_nodes(node.left)
    nodes += collect_nodes(node.right)
    return nodes


def random_node(node):
    nodes = collect_nodes(node)
    return random.choice(nodes) if nodes else node


def crossover(mrParent, msParent):
    awesomeSon  = copy.deepcopy(mrParent)
    greatDaughter  = copy.deepcopy(msParent)

    node1 = random_node(awesomeSon .root)
    node2 = random_node(greatDaughter .root)

    node1.value, node2.value = node2.value, node1.value
    node1.left, node2.left = node2.left, node1.left
    node1.right, node2.right = node2.right, node1.right

    return awesomeSon, greatDaughter


def mutate(individual, max_height=3, mutation_rate=0.1):
    if random.random() > mutation_rate:
        return individual
    mutant = copy.deepcopy(individual)
    node = random_node(mutant.root)
    new_subtree = Tree()
    new_subtree.grow(max_height)
    node.value = new_subtree.root.value
    node.left = new_subtree.root.left
    node.right = new_subtree.root.right
    return mutant
