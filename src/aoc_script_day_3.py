# Import packages
import numpy as np
import pandas as pd
import re
import os

# Functions
def make_data(dir_folder='assets',
              file_name='aoc_data_day_3.csv',
              col_name_values='values',
              col_name_binary='binary',
              col_name_position='position'):
    dir_main = os.getcwd()
    file_path="/".join([dir_main, dir_folder, file_name])
    output = pd.read_csv(file_path, header=None, names=[col_name_values])
    output[col_name_binary] = make_binary(output, col_name_values)
    output = output.convert_dtypes()

    return output

def make_binary(data, col_values):
    return data[col_values].str.replace('.', '0').str.replace('#', '1')

def make_tree_count(data, col_binary, movement_side, movement_down):
    row_length = len(data.iloc[0, 0])
    total_rows = len(data.iloc[:, 0])
    total_value = 0
    total_place = 0
    total_row = 0

    for row, value in enumerate(data[col_binary]):
        if row + movement_down >= total_rows:
            continue

        elif row != total_row:
            continue

        else:
            if total_place + movement_side >= row_length:
                total_place = total_place + movement_side - row_length
                total_row = row + movement_down
                total_value += int(
                    data.at[total_row, 'binary'][total_place]
                )

            else:
                total_place = total_place + movement_side
                total_row = row + movement_down
                total_value += int(
                    data.at[total_row, 'binary'][total_place]
                )

    return total_value

def make_tree_runs(data, col_binary, right_movements, down_movements):
    total_product = 1

    for number, right in enumerate(right_movements):
        total_product = total_product * make_tree_count(data,
                                                        col_binary,
                                                        right,
                                                        down_movements[number])

    return total_product

# Assumptions
right_values = [1, 3, 5, 7, 1]
down_values = [1, 1, 1, 1, 2]

# Import data
data = make_data()

# Measure position
print(make_tree_runs(data,
                     col_binary='binary',
                     right_movements=right_values,
                     down_movements=down_values))

print(make_tree_count(data, col_binary='binary', movement_side=7, movement_down=1))
