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

# Assumptions

# Import data
with open(file_name, newline='') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row[0] for row in reader]

data = pd.DataFrame(list(itertools.product(rows, rows))).astype(int)
data = data.rename({0: "value_1", 1: "value_2"}, axis=1)
data["add"] = data["value_1"] + data["value_2"]
data["times"] = data["value_1"] * data["value_2"]
print(data[data["add"]==2020])
