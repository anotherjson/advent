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

# Assumptions

# Import data
data = make_data()
print(data)
print(data.info())

# Measure position
row_length = len(data.iloc[0, 0])
total_rows = len(data.iloc[:, 0])
print('row_length:', row_length)
print('total_rows:', total_rows)
total_value = 0
total_place = 0
movement = 3
for row, value in enumerate(data['binary']):
    if row == total_rows - 1:
        continue
    else:
        if total_place + movement >= row_length:
            total_place = total_place + movement - row_length
            total_value += int(data.at[row + 1, 'binary'][total_place])
        else:
            total_place = total_place + movement
            total_value += int(data.at[row + 1, 'binary'][total_place])
print('total_value:', total_value)
