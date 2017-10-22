# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = "./data/ipl_matches_small.csv"
dtype = 'float64'

def read_csv_data_to_ndarray(path, dtype):
    np_arr=np.genfromtxt(path, dtype, delimiter=",", skip_header=1)
    return np_arr

read_csv_data_to_ndarray(path, dtype)
# Enter code here
