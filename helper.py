import re

def make_lambda(expr: str, variables: list):
    # remove spaces
    expr = expr.replace(" ", "")

    # insert * where needed, like 2x -> 2*x or xy -> x*y
    expr = re.sub(r'(?<=\d)(?=[a-zA-Z])', '*', expr)
    expr = re.sub(r'(?<=[a-zA-Z])(?=[a-zA-Z])', '*', expr)

    # replace variable names with indexed access:
    # x -> v[0], y -> v[1], etc.
    for i, var in enumerate(variables):
        expr = re.sub(rf'\b{var.strip()}\b', f'v[{i}]', expr)

    # build the lambda
    return eval(f"lambda v: {expr}")

def evaluate(func, input_vars: dict) -> float:
    return func(**input_vars)
