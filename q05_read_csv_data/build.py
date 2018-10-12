# %load q05_read_csv_data/build.py
# Default imports
import numpy as np
from numpy import genfromtxt

# Enter code here
path = './data/ipl_matches_small.csv'
input_dtype = '|S50'
def read_ipl_data_csv(path,dtype):
    ipl_matches_array = genfromtxt(path, dtype = dtype,delimiter=',',skip_header=1)
    np.array(ipl_matches_array)
    return ipl_matches_array

ipl_matches_array = read_ipl_data_csv('data/ipl_matches_small.csv',input_dtype)

ipl_matches_array


