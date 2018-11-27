# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
import pandas as pd



path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path, dtype = 'Float64'):
    arr = np.genfromtxt('data/ipl_matches_small.csv', dtype=dtype, skip_header=1, delimiter=',')
    return arr
read_csv_data_to_ndarray(path)


