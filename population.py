from tree.tree import Tree

def make_population(size: int, max_tree_height: int) -> list:
    population = []
    for _ in range(size):
        tree = Tree()
        # half grow and half full
        if _ % 2 == 0:
            # grow method
            tree.grow(max_height=max_tree_height)
        else:
            # full method
            tree.full(max_height=max_tree_height)
        population.append(tree)
    return population
