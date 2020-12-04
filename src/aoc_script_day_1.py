# Import packages
import numpy as np
import pandas as pd
import itertools
import csv
import os

# Create paths
dir_main = os.getcwd()
dir_file = "/".join([dir_main, "assets"])
file_name = "/".join([dir_file, "aoc_data_day_1.csv"])

# Functions
def make_iterations(data, col_names, col_add_name="add", add_value=2020):
    output = (
        pd.DataFrame(list(itertools.product(*data)), columns=col_names)
        .astype(int)
    )

    output[col_add_name] = output.sum(axis=1)

    return output[output[col_add_name]==add_value]

# Assumptions

# Import data
with open(file_name, newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row[0] for row in reader]

data_2 = make_iterations([rows, rows], col_names=["value_1", "value_2"])
data_2["multple"] = data_2["value_1"] * data_2["value_2"]
print(data_2.iloc[0])
print("----")
data_3 = make_iterations([rows, rows, rows],
                         col_names=["value_1", "value_2", "value_3"])
data_3["multiple"] = data_3["value_1"] * data_3["value_2"] * data_3["value_3"]
print(data_3.iloc[0])
