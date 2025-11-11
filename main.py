from config.config_reader import read_config
from dataset.data_reader import read_data
from helper import get_target_outputs
from population import make_population
from fitness import fitness, average_fitness, max_fitness, get_predictions
from selection.roulette import RouletteSelection
from evolve.crossover import run_crossover
from evolve.mutation import run_mutations
from plot_results import plot_average_fitness_history, plot_target_vs_final_prediction, plot_target_vs_final_prediction_2d

if __name__ == "__main__":
    target_expression, variables, data = read_data('dataset/data.csv')
    print("Target Expression:", target_expression)

    config = read_config('config/config.json')
    population = make_population(config.population_size, config.max_tree_height)

    target_outputs = get_target_outputs(target_expression, data, variables)
    average_fitness_history = []

    for generation in range(1, config.max_generations + 1):
        fitness_scores = [fitness(individual, target_outputs, data, variables) for individual in population]
        current_average_fitness = average_fitness(population, target_outputs, data, variables)
        average_fitness_history.append(current_average_fitness)
        max_fit, best_individual = max_fitness(population, target_outputs, data, variables)
        print(f"Generation {generation}: Average Fitness = {current_average_fitness}, Max Fitness = {max_fit}")
        print("Best Individual Expression:", best_individual.to_string())

        if max_fit >= 0.9: # fitness threshold
            print("Optimal solution found!")
            break

        # selection
        selector = RouletteSelection()
        parents = selector.create_parents_pool(population, fitness_scores)
        # crossover
        children = run_crossover(parents, config.population_size, config.crossover_rate)
        # mutations
        mutated_children = run_mutations(children, config.mutation_rate)
        population = mutated_children

    print("The process is completed")
    print("Elapsed generations: ", generation)
    print(average_fitness_history)
    plot_average_fitness_history(average_fitness_history)
    best_individuals_predictions = get_predictions(best_individual, data, variables)
    plot_target_vs_final_prediction(target_outputs, best_individuals_predictions)
    plot_target_vs_final_prediction_2d(target_outputs, best_individuals_predictions)
