# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'

def read_csv_data_to_ndarray(file_path,dtype):
    Numpy_array = np.genfromtxt( file_path,delimiter=',',dtype =dtype, skip_header= 1)
    return Numpy_array
# Enter code here

read_csv_data_to_ndarray(path,'float64')


