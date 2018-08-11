# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path, dtype):
    return np.genfromtxt(path, delimiter = ',', dtype = dtype, skip_header=1)

read_csv_data_to_ndarray(path, '|S100')
arr = read_csv_data_to_ndarray(path, '|S100')
print(arr.shape)
#np.reshape(arr, (1452, 23))
arr



