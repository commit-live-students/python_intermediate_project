# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np

path = './data/ipl_matches_small.csv'
def read_csv_data_to_ndarray(path, dtype):
    from numpy import genfromtxt
    my_data = genfromtxt(path, delimiter=',', skip_header=1).astype(np.float64)
    return my_data
# Enter code here





