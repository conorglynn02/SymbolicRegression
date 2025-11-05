from helper import make_lambda, evaluate
from dataset.data_reader import read_data
from config.config_reader import read_config
from population import make_population
from tree.tree import Tree
from fitness import mean_squared_error

if __name__ == "__main__":

    target_expression, guess_expression, variables, data = read_data('dataset/data.csv')
    print("Target Expression:", target_expression)
    print("Guess Expression:", guess_expression)
    print("Variables:", variables)
    print("Data sample:", data[:5])  # print first 5 rows

    target_func = make_lambda(target_expression, variables)
    guess_func = make_lambda(guess_expression, variables)

    # difference between row, *row and **row?
    # row is a list, *row unpacks the list into separate arguments, **row would unpack a dictionary
    target_outputs = [target_func(row) for row in data]
    guess_outputs = [guess_func(row) for row in data]

    for i, row in enumerate(data[:5]):  # test first 5 rows
        print(f"1. Input: {row}, Output: {target_outputs[i]}")
        print(f"2. Input: {row}, Output: {guess_outputs[i]}")

    mse = mean_squared_error(guess_outputs, target_outputs)
    print("Mean Squared Error between guess and target:", mse)

    # target_func = "2x+5y-z"
    # f = lambda x, y, z: 2*x + 3*y - z
    # target_ans = evaluate(f, {"x": 2, "y": 4, "z": 5})  # 11

    # how to do genetic programming for this target function?
    # steps:
    # 1. define a population of random functions
    # 2. define a fitness function to evaluate how close a function is to the target function, e.g., mean squared error over a set of sample inputs
    # 3. select parents from the population based on fitness
    # 4. apply genetic operators (crossover, mutation) to create a new population
    # 5. repeat steps 2-4 for a number of generations or until a satisfactory solution is found

    # config = read_config('config/config.json')
    # pop = make_population(config.population_size, config.max_tree_height)
