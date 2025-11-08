import copy
from tree.tree import Tree

def crossover(mrParent: Tree, msParent: Tree) -> tuple:
    awesomeSon  = copy.deepcopy(mrParent)
    greatDaughter  = copy.deepcopy(msParent)

    node1 = awesomeSon.random_node()
    node2 = greatDaughter.random_node()

    node1.value, node2.value = node2.value, node1.value
    node1.left, node2.left = node2.left, node1.left
    node1.right, node2.right = node2.right, node1.right

    return awesomeSon, greatDaughter
