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

def get_target_outputs(target_function: str, data: list[list[float]], variables: list[str]) -> list[float]:
    target_func = make_lambda(target_function, variables)
    outputs = []
    for row in data:
        output = target_func(row)
        outputs.append(output)
    return outputs
