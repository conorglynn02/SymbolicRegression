from tree.tree import Tree
from tree.tree_node import TreeNode

def fitness(individual: Tree, target_outputs: list[float], data: list[list[float]], variables: list[str]) -> float:
    # traverse the tree and compute the output for a set of sample inputs
    # compare the output to the target function's output
    predictions = get_predictions(individual, data, variables)
    rmse = root_mean_squared_error(predictions, target_outputs)
    return _fitness(rmse)

def total_fitness(population: list[Tree], target_outputs: list[float], data: list[list[float]], variables: list[str]) -> float:
    total = 0.0
    for individual in population:
        total += fitness(individual, target_outputs, data, variables)
    return total

def average_fitness(population: list[Tree], target_outputs: list[float], data: list[list[float]], variables: list[str]) -> float:
    return total_fitness(population, target_outputs, data, variables) / len(population)

def max_fitness(population: list[Tree], target_outputs: list[float], data: list[list[float]], variables: list[str]) -> float:
    max_fit, max_individual = float('-inf'), None
    for individual in population:
        fit = fitness(individual, target_outputs, data, variables)
        if fit > max_fit:
            max_fit = fit
            max_individual = individual
    return max_fit, max_individual

def get_predictions(tree: Tree, data: list[list[float]], variables: list[str]) -> list[float]:
    predictions = []
    var_index = {var: i for i, var in enumerate(variables)}
    for row in data:
        prediction = evaluate_tree(tree.root, row, var_index)
        predictions.append(prediction)
    return predictions

def mean_squared_error(predictions: list[float], targets: list[float]) -> float:
    if len(predictions) != len(targets):
        raise ValueError("Length of predictions and targets must be the same.")
    return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)

def root_mean_squared_error(predictions: list[float], targets: list[float]) -> float:
    if len(predictions) != len(targets):
        raise ValueError("Length of predictions and targets must be the same.")
    return (sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)) ** 0.5

def _fitness(mse: float) -> float:
    return 1 / (1 + mse)

def evaluate_tree(node: TreeNode, row: list[float], var_index: dict[str, int]) -> float:
    if node is None:
        return 0

    if node.is_leaf():
        value = node.value
        if isinstance(value, str):
            index = var_index.get(value, None)
            return row[index] if index is not None else 0
        else:
            return value

    left_value = evaluate_tree(node.left, row, var_index)
    right_value = evaluate_tree(node.right, row, var_index)

    op = node.value
    try:
        if op == '+':
            return left_value + right_value
        elif op == '-':
            return left_value - right_value
        elif op == '*':
            return left_value * right_value
        elif op == '/':
            return left_value / right_value if right_value != 0 else 1 # avoid continuous division by zero
        else:
            raise ValueError(f"Unknown operator: {op}")

    except Exception:
        return 0
