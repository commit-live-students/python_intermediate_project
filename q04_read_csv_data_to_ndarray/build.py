# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
from inspect import getfullargspec
path = './data/ipl_matches_small.csv'

# Enter code here
dtype='|S100'
def read_csv_data_to_ndarray(path, dtype):
    data = np.genfromtxt(path, dtype, skip_header=1, delimiter=',')
    return data

read_csv_data_to_ndarray(path,dtype)

