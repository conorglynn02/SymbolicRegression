# reads the data csv file and returns the target expression, variable names and data as a list of lists
# important: the first row always shows the target expression,
# the second row always shows the variable names
# and all rows must be the same length as the first row

import csv

def read_data(file_path: str) -> tuple[str, list[str], list[list[float]]]:
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        target_expression = next(reader)[0]
        # get the variable names from the second row
        variables = next(reader)
        for row in reader:
            if len(row) != len(variables):
                raise ValueError("All rows must have the same length as the header row.")
            # convert each value to float
            float_row = [float(value) for value in row]
            data.append(float_row)
    return target_expression, variables, data
