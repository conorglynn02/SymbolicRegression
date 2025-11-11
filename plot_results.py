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

def plot_target_vs_final_prediction(target_outputs: list[float], prediction: list[float]) -> None:
    os.makedirs("results", exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(target_outputs, label='Target Outputs', color='blue')
    plt.plot(prediction, label='Final Prediction', color='red', linestyle='--')
    plt.title("Target Outputs vs Final Prediction Outputs")
    plt.xlabel("Data Point Index")
    plt.ylabel("Output Value")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/target_vs_final_prediction.png")
    plt.show()
    plt.close()

def plot_target_vs_final_prediction_2d(target_outputs: list[float], prediction: list[float]) -> None:
    os.makedirs("results", exist_ok=True)

    plt.figure(figsize=(8, 8))
    plt.scatter(target_outputs, prediction, color='purple', alpha=0.6)
    plt.plot([min(target_outputs), max(target_outputs)], [min(target_outputs), max(target_outputs)], color='green', linestyle='--', label='Ideal Prediction')
    plt.title("Target Outputs vs Final Prediction Outputs (2D Scatter)")
    plt.xlabel("Target Outputs")
    plt.ylabel("Final Prediction Outputs")
    plt.legend()
    plt.grid(True)

    plt.savefig("results/target_vs_final_prediction_2d.png")
    plt.show()
    plt.close()
