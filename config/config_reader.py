import json
from dataclasses import dataclass

@dataclass
class Config:
    population_size: int
    max_tree_height: int
    max_generations: int
    selection_method: str
    crossover_rate: float
    mutation_rate: float

def read_config(file_path: str) -> Config:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return Config(**data)
