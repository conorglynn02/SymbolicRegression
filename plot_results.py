import os
import matplotlib.pyplot as plt

def plot_average_fitness_history(average_fitness_history: list) -> None:
    os.makedirs("results", exist_ok=True)

    plt.plot(average_fitness_history, marker='o')
    plt.title("Average Fitness Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Average Fitness")
    plt.grid(True)

    plt.savefig("results/average_fitness_history.png")
    plt.show()
    plt.close()
