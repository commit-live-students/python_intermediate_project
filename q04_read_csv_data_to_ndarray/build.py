# %load q04_read_csv_data_to_ndarray/build.py
# Default Imports
import numpy as np
from numpy import genfromtxt

path = './data/ipl_matches_small.csv'
input_dtype = '|S100'
# Enter code here
def read_csv_data_to_ndarray(path,input_dtype):
    my_data = genfromtxt(path, dtype = input_dtype,delimiter=',',skip_header=1)
    np.array(my_data)
    return my_data
ipl_array = read_csv_data_to_ndarray('data/ipl_matches_small.csv', input_dtype)

ipl_array


