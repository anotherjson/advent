# Import packages
import numpy as np
import pandas as pd
import itertools
import csv
import os

# Functions
def make_iterations(data, col_names, col_add_name="add", add_value=2020):
    temp = (
        pd.DataFrame(list(itertools.product(*data)), columns=col_names)
        .astype(int)
    )

    temp[col_add_name] = temp.sum(axis=1)
    output_1 = temp[temp[col_add_name]==add_value].iloc[0]

    output_2 = 0
    for row, value in enumerate(output_1[:-1]):
        if row == 0:
            output_2 += value

        else:
            output_2 += output_2 * value

    return output_1, output_2

# Assumptions
dir_name = "assets"
file_name = "aoc_data_day_1.csv"

# Create paths
dir_main = os.getcwd()
file_path = "/".join([dir_main, dir_name, file_name])

# Import data
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row[0] for row in reader]

# Calc data
print(make_iterations([rows, rows], col_names=["value_1", "value_2"]))
print("----")
print(make_iterations([rows, rows, rows],
                      col_names=["value_1", "value_2", "value_3"]))
