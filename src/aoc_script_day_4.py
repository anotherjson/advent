# Import packages
import numpy as np
import pandas as pd
import re
import csv
import os

# Functions
def import_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        rows = [row for row in reader]

    return rows

# Assumptions
dir_wd = os.getcwd()
dir_folder = 'assets'
file_name = 'aoc_data_day_4.txt'

# Import data
with open('/'.join([dir_wd, dir_folder, file_name]), 'r') as txtfile:
    data = txtfile.read()
    txtfile.close()
print(data)
