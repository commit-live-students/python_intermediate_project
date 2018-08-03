# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
# Enter code here
def read_csv_data_to_ndarray(path=path, input_dtype = np.float64):
    return np.genfromtxt(path, delimiter=',', dtype = input_dtype, skip_header=1)
read_csv_data_to_ndarray(path)



