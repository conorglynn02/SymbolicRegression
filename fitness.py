from tree.tree import Tree
from tree.tree_node import TreeNode

def fitness(individual: Tree, target_function_tree: Tree) -> list:
    # traverse the tree and compute the output for a set of sample inputs
    # compare the output to the target function's output
    predictions = get_predictions(individual)
    targets = get_predictions(target_function_tree)
    return mean_squared_error(predictions, targets)

def get_predictions(tree: Tree, func_inputs: list) -> list:
    predictions = []
    for input in func_inputs:
        prediction = evaluate_tree(tree.root, input)
        predictions.append(prediction)
    return predictions

def mean_squared_error(predictions, targets) -> float:
    if len(predictions) != len(targets):
        raise ValueError("Length of predictions and targets must be the same.")
    return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)

def evaluate_tree(node: TreeNode, input_vars: dict) -> float:
    pass

def evaluate_expression(expression:str, input_vars: dict) -> float:
    for var, value in input_vars.items():
        expression = expression.replace(var, str(value))
    try:
        result = eval(expression)
    except ZeroDivisionError:
        result = 0  # handle division by zero gracefully
    return result
