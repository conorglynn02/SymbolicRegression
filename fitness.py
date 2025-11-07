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
    if node is None:
        return 0
    
    if node.is_leaf():
        if isinstance(node.value, str):  # variable
            return node.value
        elif node.value in input_vars:  # variable in input
            return input_vars[node.value]
        else:  # constant
            return 0
    
    left_value = evaluate_tree(node.left, input_vars)
    right_value = evaluate_tree(node.right, input_vars)
    
    try:
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
        elif node.value == '*':
            return left_value * right_value
        elif node.value == '/':
            return left_value / right_value if right_value != 0 else 0
        
    except Exception:
        return 0 
    
def evaluate_expression(expression:str, input_vars: dict) -> float:
    for var, value in input_vars.items():
        expression = expression.replace(var, str(value))
    try:
        result = eval(expression)
    except ZeroDivisionError:
        result = 0  # handle division by zero gracefully
    return result
