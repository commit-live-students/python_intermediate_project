# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

# Enter code here
def read_csv_data_to_ndarray(path,dtype):
    my_data = np.genfromtxt(path, delimiter=',',skip_header=1,dtype=dtype)
    return my_data

read_csv_data_to_ndarray(path,np.float64)


