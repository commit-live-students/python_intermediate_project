# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
path = './data/ipl_matches_small.csv'
input_dtype='|S100'
# Enter code here
def read_csv_data_to_ndarray(path,input_dtype):
    ipl_array= np.genfromtxt(path,skip_header=1, delimiter=',',dtype=input_dtype)
    return ipl_array

read_csv_data_to_ndarray(path,input_dtype)

