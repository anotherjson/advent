# Import packages
import numpy as np
import pandas as pd
import re
import os

# Functions
def import_data(dir_wd,
                dir_file,
                file_name,
                col_names=['Values',
                           'Min',
                           'Max',
                           'Letter',
                           'Password',
                           'Count',
                           'Compliance_1',
                           'Compliance_2']):
    file_path = "/".join([dir_wd, dir_file, file_name])
    output = pd.read_csv(file_path, header=None, names=[col_names[0]])
    output[col_names[1:5]] = extract_data(output, col_names[0])
    output = output.convert_dtypes()
    output[col_names[1]] = output[col_names[1]].astype(float)
    output[col_names[2]] = output[col_names[2]].astype(float)
    output = count_letters(output, col_names[3], col_names[4], col_names[5])
    output[col_names[6]] = measure_compliance_one(output,
                                                  col_names[1],
                                                  col_names[2],
                                                  col_names[5])
    output = measure_compliance_two(output,
                                    col_names[1],
                                    col_names[2],
                                    col_names[3],
                                    col_names[4],
                                    col_names[7])
    return output

def extract_data(data,
                 col_values,
                 reg='(\d+)-(\d+)\s(\w+):\s(.*)'):

    return data[col_values].str.extract(reg)

def count_letters(data, col_letter, col_password, col_count):
    for row, value in enumerate(data[col_password]):
        data.at[row, col_count] = (
            value.count(data.at[row, col_letter])
        )

    return data

def measure_compliance_one(data, col_min, col_max, col_count):
    output = (
        (data[col_count]>=data[col_min]) & (data[col_count]<=data[col_max])
    )
    return output

def measure_compliance_two(data,
                           col_min,
                           col_max,
                           col_letter,
                           col_password,
                           col_compliance):
    for row, value in enumerate(data[col_password]):
        data.at[row, col_compliance] = (
            (
                (value[int(data.at[row, col_min] - 1)]==data.at[row, col_letter])
                & (value[int(data.at[row, col_max] - 1)]!=data.at[row, col_letter])
            )
            | (
                (value[int(data.at[row, col_min] - 1)]!=data.at[row, col_letter])
                & (value[int(data.at[row, col_max] - 1)]==data.at[row, col_letter])
            )
        )

    return data

# Assumptions
dir_working = os.getcwd()
dir_assets = 'assets'
file_name = 'aoc_data_day_2.csv'

# Import data
data = import_data(dir_working, dir_assets, file_name)

# Research
print(data)
print(data.info())
print(data.sum())
